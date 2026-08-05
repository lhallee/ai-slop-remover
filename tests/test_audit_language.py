"""Tests for the advisory language checker."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest

from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
CHECKER = REPOSITORY_ROOT / "skills" / "writing-standards" / "scripts" / "audit_language.py"
FIXTURES = Path(__file__).parent / "fixtures"


class AuditLanguageTests(unittest.TestCase):
    def run_checker(
        self,
        path: Path,
        output_format: str = "json",
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(CHECKER), str(path), "--format", output_format],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_reports_terms_phrases_and_em_dash(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            document = Path(temp_directory) / "draft.md"
            document.write_text(
                "We leverage a robust framework. It is important to note the result. "
                "The claim\u2014which lacks a source\u2014should be narrower.",
                encoding="utf-8",
            )

            completed = self.run_checker(document)
            findings = json.loads(completed.stdout)
            rules = {finding["rule"] for finding in findings}

            self.assertEqual(completed.returncode, 0)
            self.assertIn("context-leverage", rules)
            self.assertIn("context-robust", rules)
            self.assertIn("empty-transition", rules)
            self.assertIn("prohibited-em-dash", rules)

    def test_inspects_python_identifiers_comments_and_strings(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            module = Path(temp_directory) / "module.py"
            module.write_text(
                '"""A realm of possibilities.\u2014No."""\n'
                "def robust_pipeline():\n"
                "    load_bearing_helper = RobustPipeline\n"
                "    message = 'It is robust, seamless, and transformative.'\n"
                "    # Delve into the records.\n"
                "    return f'pivotal {load_bearing_helper}'\n",
                encoding="utf-8",
            )

            completed = self.run_checker(module)
            findings = json.loads(completed.stdout)
            rules = {finding["rule"] for finding in findings}

            self.assertEqual(completed.returncode, 0)
            self.assertIn("context-robust", rules)
            self.assertIn("default-avoid-load-bearing", rules)
            self.assertIn("default-avoid-delve", rules)
            self.assertIn("default-avoid-realm", rules)
            self.assertIn("default-avoid-pivotal", rules)
            self.assertIn("prohibited-em-dash", rules)
            self.assertIn("decorative-adjective-triad", rules)

    def test_flags_repeated_openings_and_decorative_triads(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            document = Path(temp_directory) / "patterns.txt"
            document.write_text(
                "The model can read records. The model can write records. "
                "The model can delete records. It is robust, seamless, and transformative.",
                encoding="utf-8",
            )

            completed = self.run_checker(document)
            findings = json.loads(completed.stdout)
            rules = {finding["rule"] for finding in findings}

            self.assertIn("repeated-sentence-opening", rules)
            self.assertIn("decorative-adjective-triad", rules)

    def test_supported_text_formats(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            for suffix in (".md", ".rst", ".tex", ".txt"):
                with self.subTest(suffix=suffix):
                    document = Path(temp_directory) / f"draft{suffix}"
                    document.write_text("We leverage the result.\n", encoding="utf-8")

                    completed = self.run_checker(document)
                    findings = json.loads(completed.stdout)

                    self.assertEqual(completed.returncode, 0)
                    self.assertEqual(findings[0]["rule"], "context-leverage")
                    self.assertEqual(
                        set(findings[0]),
                        {"path", "line", "column", "match", "rule", "severity"},
                    )

    def test_text_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            document = Path(temp_directory) / "draft.md"
            document.write_text("We leverage the result.\n", encoding="utf-8")

            completed = self.run_checker(document, output_format="text")

            self.assertEqual(completed.returncode, 0)
            self.assertIn("info context-leverage", completed.stdout)
            self.assertIn(":1:4:", completed.stdout)

    def test_context_terms_are_informational(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            document = Path(temp_directory) / "technical.md"
            document.write_text(
                "The manifest records the provenance of each training shard. "
                "The method was robust across five seeds.\n",
                encoding="utf-8",
            )

            completed = self.run_checker(document)
            findings = json.loads(completed.stdout)
            severities = {finding["rule"]: finding["severity"] for finding in findings}

            self.assertEqual(severities["context-provenance"], "info")
            self.assertEqual(severities["context-robust"], "info")

    def test_skips_environment_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            root = Path(temp_directory)
            skipped = root / ".venv"
            skipped.mkdir()
            (skipped / "generated.py").write_text("# Delve into this realm.\n", encoding="utf-8")
            (root / "clean.md").write_text("The test passed under three seeds.\n", encoding="utf-8")

            completed = self.run_checker(root)

            self.assertEqual(json.loads(completed.stdout), [])

    def test_does_not_modify_input(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            document = Path(temp_directory) / "draft.md"
            original = "This robust method needs a more exact description.\n"
            document.write_text(original, encoding="utf-8")

            self.run_checker(document)

            self.assertEqual(document.read_text(encoding="utf-8"), original)

    def test_notation_fixtures_are_clean(self) -> None:
        completed = self.run_checker(FIXTURES)

        self.assertEqual(completed.returncode, 0)
        self.assertEqual(json.loads(completed.stdout), [])

    def test_missing_path_returns_error(self) -> None:
        completed = self.run_checker(Path("missing-audit-target"))

        self.assertEqual(completed.returncode, 2)
        self.assertEqual(json.loads(completed.stdout), [])
        self.assertIn("Path does not exist", completed.stderr)

    def test_absolute_checker_path_works_from_unrelated_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_directory:
            root = Path(temp_directory)
            installed_root = root / "installed-skills"
            shutil.copytree(REPOSITORY_ROOT / "skills", installed_root)
            checker = (
                installed_root
                / "writing-standards"
                / "scripts"
                / "audit_language.py"
            )
            work_directory = root / "project"
            work_directory.mkdir()
            document = work_directory / "draft.md"
            document.write_text("We leverage the result.\n", encoding="utf-8")

            completed = subprocess.run(
                [sys.executable, str(checker), str(document), "--format", "json"],
                cwd=work_directory,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(completed.returncode, 0)
            self.assertEqual(json.loads(completed.stdout)[0]["rule"], "context-leverage")

    @unittest.skipUnless(
        sys.platform == "win32" and shutil.which("powershell"),
        "Windows PowerShell is required",
    )
    def test_absolute_python_resolver_path_works_from_unrelated_directory(self) -> None:
        resolver = (
            REPOSITORY_ROOT
            / "skills"
            / "apply-coding-standards"
            / "scripts"
            / "resolve_python.ps1"
        )
        with tempfile.TemporaryDirectory() as temp_directory:
            root = Path(temp_directory)
            installed_root = root / "installed-skills"
            shutil.copytree(REPOSITORY_ROOT / "skills", installed_root)
            completed = subprocess.run(
                [
                    "powershell",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    str(
                        installed_root
                        / "apply-coding-standards"
                        / "scripts"
                        / resolver.name
                    ),
                    "-ProjectPath",
                    str(root),
                ],
                cwd=root,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(completed.returncode, 0, completed.stderr)
            resolved = json.loads(completed.stdout)
            self.assertIn("Python", resolved["version"])


if __name__ == "__main__":
    unittest.main()
