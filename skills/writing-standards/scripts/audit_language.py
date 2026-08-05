"""Report mechanical language signals for contextual review."""

import argparse
import io
import json
import os
import re
import sys
import tokenize

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Iterator


SUPPORTED_SUFFIXES = {".md", ".markdown", ".py", ".rst", ".tex", ".txt"}
PYTHON_TEXT_TOKENS = {
    tokenize.COMMENT,
    tokenize.STRING,
    getattr(tokenize, "FSTRING_MIDDLE", -1),
}
SKIP_DIRECTORIES = {
    ".git",
    ".hg",
    ".mypy_cache",
    ".nox",
    ".pytest_cache",
    ".ruff_cache",
    ".svn",
    ".tox",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "env",
    "node_modules",
    "site-packages",
    "vendor",
    "venv",
}


@dataclass(frozen=True)
class Rule:
    name: str
    severity: str
    pattern: re.Pattern[str]


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    column: int
    match: str
    rule: str
    severity: str


def compile_rule(name: str, severity: str, pattern: str) -> Rule:
    return Rule(name, severity, re.compile(pattern, re.IGNORECASE))


TERM_RULES = (
    compile_rule("default-avoid-delve", "warning", r"\bdelv(?:e|es|ed|ing)\b"),
    compile_rule("default-avoid-tapestry", "warning", r"\btapestr(?:y|ies)\b"),
    compile_rule("default-avoid-realm", "warning", r"\brealms?\b"),
    compile_rule("default-avoid-showcase", "warning", r"\bshowcas(?:e|es|ed|ing)\b"),
    compile_rule("default-avoid-underscore", "warning", r"\bunderscor(?:e|es|ed|ing)\b"),
    compile_rule("default-avoid-intricate", "warning", r"\b(?:intricate|intricacy|intricacies)\b"),
    compile_rule("default-avoid-pivotal", "warning", r"\bpivotal\b"),
    compile_rule("default-avoid-groundbreaking", "warning", r"\bgroundbreaking\b"),
    compile_rule("default-avoid-load-bearing", "warning", r"\bload[-_\s]+bearing\b"),
    compile_rule("context-provenance", "info", r"\bprovenance\b"),
    compile_rule("context-robust", "info", r"\brobust(?:ness)?\b"),
    compile_rule("context-significant", "info", r"\bsignifican(?:t|ce|tly)\b"),
    compile_rule("context-comprehensive", "info", r"\bcomprehensive(?:ly)?\b"),
    compile_rule("context-crucial", "info", r"\bcrucial(?:ly)?\b"),
    compile_rule("context-landscape", "info", r"\blandscapes?\b"),
    compile_rule("context-leverage", "info", r"\bleverag(?:e|es|ed|ing)\b"),
    compile_rule("context-foster", "info", r"\bfoster(?:s|ed|ing)?\b"),
    compile_rule("context-align", "info", r"\balign(?:s|ed|ing|ment|ments)?\b"),
    compile_rule("context-potential", "info", r"\bpotential(?:ly)?\b"),
)

PHRASE_RULES = (
    compile_rule("prohibited-em-dash", "error", "\u2014"),
    compile_rule("empty-transition", "warning", r"\bit is (?:important|worth) (?:to note|noting)\b"),
    compile_rule("generic-evolving-opening", "warning", r"\bin today(?:'|\u2019)s rapidly (?:changing|evolving)\b"),
    compile_rule("contrast-template-not-just", "warning", r"\bnot just\b[^.!?\n]{0,120}\bbut\b"),
    compile_rule("contrast-template-not-only", "warning", r"\bnot only\b[^.!?\n]{0,120}\bbut also\b"),
    compile_rule("ceremonial-summary", "warning", r"\b(?:in conclusion|in summary)\b"),
    compile_rule("generic-future-claim", "warning", r"\bpaving the way\b"),
    compile_rule(
        "participial-restatement",
        "warning",
        r",\s+(?:highlighting|underscoring|showcasing|demonstrating|emphasizing)\b",
    ),
)

DECORATIVE_ADJECTIVES = {
    "comprehensive",
    "crucial",
    "diverse",
    "elegant",
    "groundbreaking",
    "intricate",
    "meaningful",
    "pivotal",
    "powerful",
    "robust",
    "seamless",
    "transformative",
    "valuable",
    "vibrant",
}

TRIAD_PATTERN = re.compile(
    r"\b([A-Za-z]+)\s*,\s*([A-Za-z]+)\s*,?\s+(?:and|or)\s+([A-Za-z]+)\b"
)
SENTENCE_PATTERN = re.compile(r"(?:^|[.!?]\s+)([A-Za-z][^.!?\n]{10,})", re.MULTILINE)
WORD_PATTERN = re.compile(r"[A-Za-z]+")
IDENTIFIER_PART_PATTERN = re.compile(
    r"[A-Z]+(?=[A-Z][a-z]|[0-9]|$)|[A-Z]?[a-z]+|[A-Z]+|[0-9]+"
)


def position_for_offset(text: str, offset: int, base_line: int, base_column: int) -> tuple[int, int]:
    prefix = text[:offset]
    line_breaks = prefix.count("\n")
    if line_breaks == 0:
        return base_line, base_column + offset

    column = len(prefix.rsplit("\n", 1)[-1]) + 1
    return base_line + line_breaks, column


def normalize_match(value: str) -> str:
    return " ".join(value.split())


def scan_rules(
    text: str,
    path: Path,
    rules: Iterable[Rule],
    base_line: int = 1,
    base_column: int = 1,
) -> list[Finding]:
    findings: list[Finding] = []
    for rule in rules:
        for match in rule.pattern.finditer(text):
            line, column = position_for_offset(text, match.start(), base_line, base_column)
            findings.append(
                Finding(
                    path=str(path),
                    line=line,
                    column=column,
                    match=normalize_match(match.group(0)),
                    rule=rule.name,
                    severity=rule.severity,
                )
            )

    return findings


def scan_adjective_triads(
    text: str,
    path: Path,
    base_line: int = 1,
    base_column: int = 1,
) -> list[Finding]:
    findings: list[Finding] = []
    for match in TRIAD_PATTERN.finditer(text):
        adjectives = {word.lower() for word in match.groups()}
        if not adjectives.issubset(DECORATIVE_ADJECTIVES):
            continue

        line, column = position_for_offset(
            text,
            match.start(),
            base_line,
            base_column,
        )
        findings.append(
            Finding(
                path=str(path),
                line=line,
                column=column,
                match=match.group(0),
                rule="decorative-adjective-triad",
                severity="warning",
            )
        )

    return findings


def scan_repeated_openings(
    text: str,
    path: Path,
    base_line: int = 1,
    base_column: int = 1,
) -> list[Finding]:
    occurrences: dict[str, list[tuple[int, str]]] = {}
    for match in SENTENCE_PATTERN.finditer(text):
        words = WORD_PATTERN.findall(match.group(1).lower())
        if len(words) < 3:
            continue

        opening = " ".join(words[:3])
        occurrences.setdefault(opening, []).append((match.start(1), opening))

    findings: list[Finding] = []
    for opening, matches in occurrences.items():
        if len(matches) < 3:
            continue

        offset, _ = matches[2]
        line, column = position_for_offset(text, offset, base_line, base_column)
        findings.append(
            Finding(
                path=str(path),
                line=line,
                column=column,
                match=opening,
                rule="repeated-sentence-opening",
                severity="warning",
            )
        )

    return findings


def scan_human_text(
    text: str,
    path: Path,
    base_line: int = 1,
    base_column: int = 1,
) -> list[Finding]:
    findings = scan_rules(
        text,
        path,
        TERM_RULES + PHRASE_RULES,
        base_line,
        base_column,
    )
    findings.extend(scan_adjective_triads(text, path, base_line, base_column))
    findings.extend(scan_repeated_openings(text, path, base_line, base_column))
    return findings


def scan_plain_text(text: str, path: Path) -> list[Finding]:
    return scan_human_text(text, path)


def scan_identifier(identifier: str, path: Path, line: int, column: int) -> list[Finding]:
    parts: list[tuple[str, int]] = []
    for underscore_part in re.finditer(r"[^_]+", identifier):
        for camel_part in IDENTIFIER_PART_PATTERN.finditer(underscore_part.group(0)):
            parts.append(
                (
                    camel_part.group(0),
                    underscore_part.start() + camel_part.start(),
                )
            )

    if not parts:
        return []

    normalized = " ".join(value for value, _ in parts)
    normalized_starts: list[int] = []
    offset = 0
    for value, _ in parts:
        normalized_starts.append(offset)
        offset += len(value) + 1

    findings: list[Finding] = []
    for rule in TERM_RULES:
        for match in rule.pattern.finditer(normalized):
            part_index = max(
                index
                for index, normalized_start in enumerate(normalized_starts)
                if normalized_start <= match.start()
            )
            original_offset = parts[part_index][1]
            findings.append(
                Finding(
                    path=str(path),
                    line=line,
                    column=column + original_offset,
                    match=normalize_match(match.group(0)),
                    rule=rule.name,
                    severity=rule.severity,
                )
            )

    return findings


def scan_python(text: str, path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        tokens = tokenize.generate_tokens(io.StringIO(text).readline)
        for token in tokens:
            if token.type == tokenize.NAME:
                findings.extend(
                    scan_identifier(
                        token.string,
                        path,
                        line=token.start[0],
                        column=token.start[1] + 1,
                    )
                )
            elif token.type in PYTHON_TEXT_TOKENS:
                findings.extend(
                    scan_human_text(
                        token.string,
                        path,
                        base_line=token.start[0],
                        base_column=token.start[1] + 1,
                    )
                )
    except (IndentationError, tokenize.TokenError):
        return scan_plain_text(text, path)

    return findings


def iter_supported_files(target: Path) -> Iterator[Path]:
    if target.is_file():
        if target.suffix.lower() in SUPPORTED_SUFFIXES:
            yield target
        return

    for root, directories, filenames in os.walk(target):
        directories[:] = sorted(
            name for name in directories if name.lower() not in SKIP_DIRECTORIES
        )
        root_path = Path(root)
        for filename in sorted(filenames):
            path = root_path / filename
            if path.suffix.lower() in SUPPORTED_SUFFIXES:
                yield path


def audit_path(target: Path) -> tuple[list[Finding], list[str]]:
    findings: list[Finding] = []
    errors: list[str] = []

    if not target.exists():
        return [], [f"Path does not exist: {target}"]

    for path in iter_supported_files(target):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as error:
            errors.append(f"Could not read {path}: {error}")
            continue

        if path.suffix.lower() == ".py":
            findings.extend(scan_python(text, path))
        else:
            findings.extend(scan_plain_text(text, path))

    unique_findings = sorted(
        set(findings),
        key=lambda finding: (
            finding.path.lower(),
            finding.line,
            finding.column,
            finding.severity,
            finding.rule,
        ),
    )
    return unique_findings, errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="File or directory to inspect")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser.parse_args()


def print_text(findings: list[Finding]) -> None:
    if not findings:
        print("No findings.")
        return

    for finding in findings:
        print(
            f"{finding.path}:{finding.line}:{finding.column}: "
            f"{finding.severity} {finding.rule}: {finding.match!r}"
        )


def main() -> int:
    args = parse_args()
    findings, errors = audit_path(args.path)

    if args.format == "json":
        print(json.dumps([asdict(finding) for finding in findings], indent=2))
    else:
        print_text(findings)

    for error in errors:
        print(error, file=sys.stderr)

    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
