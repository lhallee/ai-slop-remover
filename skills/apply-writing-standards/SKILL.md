---
name: apply-writing-standards
description: Draft, revise, or audit prose with the suite's writing standards and medium-specific best practices. Use for scientific publications, blogs, essays, social posts, LinkedIn and outreach, grants and reports, peer reviews, career materials, and meeting talk tracks. Strengthen hooks, stakes, storytelling, and outcomes while preserving source fidelity, authorial voice, user edits, and the requested audience and medium.
---

# Apply Writing Standards

Produce a compelling, complete piece that fits its medium, audience, evidence, and purpose. Remove words that do no work, while keeping the context and voice that make the piece worth reading.

## Load the standards

Confirm that `../coding-standards/SKILL.md`, `../writing-standards/SKILL.md`, and `../apply-coding-standards/SKILL.md` exist. If any sibling is missing, stop and tell the user to install the complete four-skill suite.

Read `../writing-standards/SKILL.md` and every resource it requires.

## Select the operation

- **Draft:** create new prose only from supplied or verified facts.
- **Revise:** preserve the source's meaning while improving correctness, concision, structure, tone, and medium fit.
- **Audit:** report actionable standards violations without rewriting unless the user asks.

Identify the audience, medium, evidence class, requested form, and shortest sufficient length. Ask for missing facts when the gap would change the result. Otherwise use a visible placeholder or narrow the claim.

## Select the medium

Choose one primary profile and at most one secondary profile. Read only the relevant reference:

- Scientific papers, abstracts, methods, results, discussions, conclusions, limitations, captions, and journal responses: `references/scientific-publications.md`
- Technical or speculative blogs and essays: `references/blogs.md`
- LinkedIn feed posts, other social posts, launch notes, direct outreach, and short public updates: `references/linkedin-outreach.md`
- Grant proposals, progress reports, final reports, impact statements, and funder responses: `references/grants-reports.md`
- Journal reviews, editorial notes, reviewer responses, and methodological critiques: `references/peer-review.md`
- Bios, CV summaries, cover letters, application answers, and professional statements: `references/career-materials.md`
- Spoken explanations, slide narration, objections, and claim cleanup: `references/meeting-talk-tracks.md`

## Draft or revise

For blogs, essays, social posts, and launch stories, read `../writing-standards/references/storytelling.md`. Choose the strongest truthful angle for the reader, then connect the hook, problem, why, action, outcome, and goal. Draw on the relevant story pillars without forcing all six. Treat a LinkedIn article as a blog, not an elongated feed post. Treat direct outreach as a personal message, not a public story.

For other forms, start with the actual object, result, decision, or thesis. Add the evidence and explanation the reader needs. Keep qualifications beside the claims they limit. Use the shared mathematical notation in equations, captions, and prose.

For revision, read the source first and preserve user edits, useful voice, technical terminology, and deliberate structure. Respect a minimal-edit request. Cut repetition, but add a missing connection or necessary stakes when that solves the actual problem. Do not make informal writing uniformly formal or make scientific writing artificially casual.

For technical and speculative blogs, use a light humorous beat when it fits the subject and audience. Let it clarify an analogy, release tension after a dense passage, or acknowledge uncertainty. Do not force a joke or soften a measured result.

## Audit and finish

Run the advisory checker when the text exists in a supported file:

```text
python <absolute-writing-standards-dir>/scripts/audit_language.py <path>
```

Resolve `<absolute-writing-standards-dir>` from the sibling `writing-standards/SKILL.md`. Do not assume that the shell's working directory is a skill directory.

Then check:

- For public stories, does the opening earn attention from this audience, does the problem have clear stakes, and does the outcome fulfill the hook? Apply the storytelling reference's review before word-level cleanup.
- Does every fact, metric, citation, date, and publication status come from a source?
- Does claim strength match the evidence?
- Does mathematical notation remain consistent?
- Can any sentence, paragraph, heading, table, example, or conclusion be removed without losing meaning?
- Does the tone fit the actual audience and medium?
- For blogs, is there a natural light humorous beat, unless the subject or audience makes one inappropriate?
- Does the piece disclose private information that the target output does not require?

Return only the requested artifact unless a material limitation or unresolved source issue must be reported.
