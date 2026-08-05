---
name: writing-standards
description: Apply concise, correct, evidence-led writing standards while drafting, editing, or reviewing prose. Use when a user asks Codex to follow the suite's shared standards for concision, claims, attribution, terminology, mathematical notation, direct language, or avoidance of AI-associated wording in scientific, technical, professional, public, or code-facing writing. Use apply-writing-standards for a medium-specific drafting, revision, or audit workflow.
---

# Writing Standards

Write the shortest complete version that preserves the idea, evidence, and necessary nuance.

## Load the canonical rules

Confirm that `../coding-standards/SKILL.md`, `../apply-coding-standards/SKILL.md`, and `../apply-writing-standards/SKILL.md` exist. If any sibling is missing, stop and tell the user to install the complete four-skill suite.

Read `references/shared-standards.md` for concision, evidence, terminology, and mathematical notation. Read `references/ai-language.md` whenever drafting or editing human-facing language.

Treat these references as canonical for the full suite. Other skills may extend them for a domain, but must not redefine them.

## Build the argument directly

Use this progression when it fits the material:

1. Name the object or problem.
2. State the result, decision, or thesis.
3. Give the evidence or mechanism.
4. Explain the consequence.
5. Bound the claim.
6. Stop.

Give each paragraph one conceptual move. Start a new paragraph for a new result, scale, objection, caveat, or interpretation. Prefer ordinary verbs around precise technical nouns.

Put measurements, controls, citations, and limitations beside the claim they qualify. Do not let model output silently become experimental truth. Do not invent facts, citations, metrics, dates, affiliations, quotations, publication status, or validation.

Permit depth and elegance when they improve understanding. Remove repeated conclusions, ceremonial summaries, generic openings, decorative structure, and lists of adjacent possibilities.

Use `apply-writing-standards` when the request needs a medium-specific workflow for a scientific publication, blog, LinkedIn post, grant, report, peer review, career document, or meeting talk track.
