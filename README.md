# AI Slop Remover

AI Slop Remover is a Codex skill that makes working Python easier to maintain without changing its intended behavior. It uses direct control flow, precise types, domain language, clear module boundaries, and complete tensor-shape traces. It also requires ASD-STE100 Simplified Technical English for documentation.

## Install with Codex

Give this link to Codex:

```text
https://github.com/lhallee/ai-slop-remover/tree/main/skills/ai-slop-remover
```

Then ask:

```text
Install the Codex skill from this GitHub link.
```

Codex can use its `skill-installer` workflow to install the skill. The skill is available on the next turn after installation.

## Install with the Codex helper script

Run the installer supplied with Codex:

```text
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --url https://github.com/lhallee/ai-slop-remover/tree/main/skills/ai-slop-remover
```

On Windows PowerShell, run:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --url https://github.com/lhallee/ai-slop-remover/tree/main/skills/ai-slop-remover
```

Restart Codex or start a new task after installation.

## Use the skill

Invoke the skill by name:

```text
Use $ai-slop-remover to simplify this working Python without changing behavior.
```

## Repository layout

The installable skill is in [`skills/ai-slop-remover`](skills/ai-slop-remover). It includes the skill instructions, UI metadata, reference documents, and the Windows Python resolver.

## License

This repository uses the MIT License. See [`LICENSE`](LICENSE).
