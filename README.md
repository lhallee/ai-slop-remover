# Coding and Writing Standards

Coding and Writing Standards is a four-skill Codex suite for direct Python, purposeful prose, evidence-based claims, consistent mathematical notation, and behavior-preserving cleanup workflows.

For blogs and social posts, the suite addresses story selection and structure as well as sentence cleanup: a hook, a problem worth caring about, the action and outcome, and the goal. [Storytelling guidance](skills/writing-standards/references/storytelling.md) uses timing, significance, proximity, prominence, human interest, and novelty to choose a relevant angle without forcing every pillar into every piece. The [blog](skills/apply-writing-standards/references/blogs.md) and [social post](skills/apply-writing-standards/references/linkedin-outreach.md) profiles adapt that guidance to the medium.

## Install all four skills

Ask Codex:

```text
Install all four Codex skills from https://github.com/lhallee/ai-slop-remover:
skills/coding-standards
skills/writing-standards
skills/apply-coding-standards
skills/apply-writing-standards
```

Or use the Codex installer directly:

```text
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo lhallee/ai-slop-remover --path skills/coding-standards skills/writing-standards skills/apply-coding-standards skills/apply-writing-standards
```

On Windows PowerShell:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo lhallee/ai-slop-remover --path skills/coding-standards skills/writing-standards skills/apply-coding-standards skills/apply-writing-standards
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
