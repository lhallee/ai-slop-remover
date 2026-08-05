---
name: coding-standards
description: Apply concise, evidence-based Python coding standards while creating, editing, or reviewing code. Use when a user asks Codex to follow the suite's coding standards for imports, typing, control flow, naming, comments, documentation, numerical notation, tensor-shape traces, module design, or maintainable Python. Use apply-coding-standards instead for a behavior-preserving conversion workflow over existing code.
---

# Coding Standards

Write Python that exposes its data flow and intent. Prefer direct code, precise domain language, and the smallest structure that remains easy to verify.

## Load the shared standards

Confirm that `../writing-standards/SKILL.md`, `../apply-coding-standards/SKILL.md`, and `../apply-writing-standards/SKILL.md` exist. If any sibling is missing, stop and tell the user to install the complete four-skill suite.

Read `../writing-standards/references/shared-standards.md` before applying this skill. Read `../writing-standards/references/ai-language.md` when comments, docstrings, documentation, identifiers, CLI text, or other human-facing language are in scope.

If either sibling resource is missing, stop and tell the user to install the complete four-skill suite. Do not silently recreate or approximate the shared rules.

Apply this precedence:

1. Follow the user's requested behavior and scope.
2. Preserve correctness, security, public interfaces, schemas, and tested behavior.
3. Follow repository instructions and enforced tooling.
4. Apply the shared and coding standards.
5. Minimize unrelated churn.

## Organize imports

Keep a module docstring first and `from __future__ import ...` statements immediately after it. Put every direct `import ...` statement before every ordinary `from ... import ...` statement. Within each statement-type block, order standard-library, third-party, and repository-local names. Use a blank line to make a repository-local subgroup clear when present.

```python
import argparse
import numpy as np
import torch

from pathlib import Path
from torch import Tensor

from .workflow import TrainingWorkflow
```

Leave two blank lines after the complete import block. Preserve guarded, optional, registration, and initialization-sensitive imports as ordering barriers. Follow an enforced formatter or linter when it conflicts with this preference.

## Prefer direct, typed code

- Give each function one narrow responsibility and precise parameter and return types.
- Use concrete domain types and parameterized containers. Use `Any` only at a genuinely dynamic boundary.
- Respect the project's supported Python versions and typing conventions.
- Write for supported inputs. Keep defensive branches only when they protect a real requirement.
- Raise ordinary exceptions for invalid external input. Use assertions for internal invariants.
- Separate distinct guards, loops, exception handling, and logical phases when the spacing improves scanning.
- Avoid broad exception handling, silent fallback cascades, speculative compatibility paths, and wrappers that only rename another call.
- Extract a one-use helper only when it names a real concept or isolates a separately testable phase.

## Name code by meaning

- Prefer domain names over vague names such as `data`, `result`, `info`, or `manager`.
- Use lowercase snake case for descriptive variables regardless of rank, such as `hidden_states` and `attention_mask`.
- Apply the shared scalar, vector, matrix, and tensor capitalization rules to short mathematical symbols.
- Keep descriptive all-caps configuration near the top of runnable modules when it is genuinely constant.
- Preserve public names, serialized fields, framework-discovered attributes, and established external notation.

## Write for maintainers

- Make code, comments, docstrings, error messages, and documentation as short as their purpose permits.
- Apply STE-inspired clarity to code-facing prose: use direct sentences, simple verb forms, stable terminology, and American English.
- Do not claim ASD-STE100 compliance or depend on a controlled dictionary.
- Comment intent, assumptions, units, biological conventions, non-obvious mechanics, and design decisions.
- Remove prose that narrates syntax or repeats a precise name and type.
- Base claims about performance, compatibility, deprecation, tensor shapes, and behavior on code, tests, configuration, benchmarks, or current authoritative documentation.
- Preserve an exact technical term even when it appears on the language watchlist. Remove vague or decorative use.

## Trace numerical shapes

Read and apply `references/numerical-python.md` for NumPy, PyTorch, JAX, or similar array code. Treat complete and accurate shape traces as required within the selected numerical scope. Never invent a dimension or fixed rank.

## Keep structure cohesive

- Give each module one primary responsibility.
- Split by ownership and dependency direction, not line count.
- Keep helpers near the feature that owns them. Do not create catch-all utility modules.
- Give extracted modules a small intentional public surface.
- Use a class when state and behavior form a meaningful domain object or workflow. Prefer a function or typed value for simple transformations and records.
- Keep entry points thin: parse, construct, invoke a visible sequence, and report.

For a review or behavior-preserving cleanup of existing Python, use `apply-coding-standards` instead of expanding this standards skill into a conversion workflow.
