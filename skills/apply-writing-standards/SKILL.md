---
name: apply-writing-standards
description: Draft, revise, or audit prose with the suite's writing standards and medium-specific best practices. Use for scientific publications, technical or speculative blogs, LinkedIn and outreach, grants and reports, peer reviews, career materials, bios, and meeting talk tracks, especially when the user asks to apply or convert text to the writing standards. Preserve source fidelity, claim boundaries, concise structure, and the requested audience and medium.
---

# Apply Writing Standards

Produce the shortest complete piece that fits its medium, audience, evidence, and purpose.

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
- LinkedIn posts, launch notes, direct outreach, and short public updates: `references/linkedin-outreach.md`
- Grant proposals, progress reports, final reports, impact statements, and funder responses: `references/grants-reports.md`
- Journal reviews, editorial notes, reviewer responses, and methodological critiques: `references/peer-review.md`
- Bios, CV summaries, cover letters, application answers, and professional statements: `references/career-materials.md`
- Spoken explanations, slide narration, objections, and claim cleanup: `references/meeting-talk-tracks.md`

## Draft or revise

Start with the actual object, result, decision, or thesis. Add only the evidence and explanation the reader needs. Keep qualifications beside the claims they limit. Use the shared mathematical notation in equations, captions, and prose.

For revision, remove content before adding content. Preserve useful voice, technical terminology, and deliberate structure. Do not make informal writing uniformly formal or make scientific writing artificially casual.

For technical and speculative blogs, use a light humorous beat when it fits the subject and audience. Let it clarify an analogy, release tension after a dense passage, or acknowledge uncertainty. Do not force a joke or soften a measured result.

## Audit and finish

Run the advisory checker when the text exists in a supported file:

```text
python <absolute-writing-standards-dir>/scripts/audit_language.py <path>
```

Resolve `<absolute-writing-standards-dir>` from the sibling `writing-standards/SKILL.md`. Do not assume that the shell's working directory is a skill directory.

Then check:

- Does every fact, metric, citation, date, and publication status come from a source?
- Does claim strength match the evidence?
- Does mathematical notation remain consistent?
- Can any sentence, paragraph, heading, table, example, or conclusion be removed without losing meaning?
- Does the tone fit the actual audience and medium?
- For blogs, is there a natural light humorous beat, unless the subject or audience makes one inappropriate?
- Does the piece disclose private information that the target output does not require?

Return only the requested artifact unless a material limitation or unresolved source issue must be reported.
