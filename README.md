# Coding and Writing Standards

Coding and Writing Standards is a four-skill Codex suite for direct Python, concise prose, evidence-based claims, consistent mathematical notation, and behavior-preserving cleanup workflows.

## Install all four skills

Ask Codex:

```text
Install all four Codex skills from https://github.com/lhallee/coding-and-writing-standards:
skills/coding-standards
skills/writing-standards
skills/apply-coding-standards
skills/apply-writing-standards
```

Or use the Codex installer directly:

```text
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo lhallee/coding-and-writing-standards --path skills/coding-standards skills/writing-standards skills/apply-coding-standards skills/apply-writing-standards
```

On Windows PowerShell:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo lhallee/coding-and-writing-standards --path skills/coding-standards skills/writing-standards skills/apply-coding-standards skills/apply-writing-standards
```

Start a new Codex task after installation.

## Use the suite

```text
Use $coding-standards while implementing this Python change.
```

```text
Use $writing-standards to draft this text concisely and correctly.
```

```text
Use $apply-coding-standards to convert this working Python without changing behavior.
```

```text
Use $apply-writing-standards to draft, revise, or audit this piece for its medium and audience.
```

The application skills require their sibling standards skills. Install the complete suite even if you expect to invoke only one workflow.

## Migrate from the previous skills

Install this suite, start a new Codex task, and test the new invocations. Then remove an installed copy of `ai-slop-remover` if it is present and no longer needed. Installation does not alter any existing personal skills.

## Language checker

The writing standards include a non-destructive advisory checker:

```text
python skills/writing-standards/scripts/audit_language.py <file-or-directory>
```

The checker reports em dashes, AI-associated terms, stock phrases, repeated sentence openings, and decorative adjective lists. It does not edit files or determine whether text was written by AI.

## License

This repository uses the MIT License. See [LICENSE](LICENSE).
