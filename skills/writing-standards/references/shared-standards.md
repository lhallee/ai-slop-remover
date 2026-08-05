# Shared standards

Use these rules across code, documentation, mathematical notation, and prose. Domain skills may add constraints, but must not contradict them.

## Resolve conflicts

Apply rules in this order:

1. Follow the user's explicit request and scope.
2. Preserve correctness, safety, source fidelity, public behavior, and required interfaces.
3. Follow repository, venue, and enforced tool requirements.
4. Apply these standards and the selected domain profile.
5. Minimize unrelated change.

## Be concise

- Use the shortest complete implementation or explanation.
- Require every sentence, paragraph, section, example, table, helper, abstraction, and module to add information, clarify reasoning, or reduce material risk.
- Remove repeated conclusions, narrative comments, decorative structure, unnecessary examples, speculative abstractions, and wrappers that only rename another operation.
- Prefer one clear paragraph over a report-shaped answer when one paragraph is sufficient.
- Add length only to explain a difficult mechanism, establish evidence, preserve necessary nuance, or communicate an elegant idea clearly.
- Obey a required format or length, but do not fill available space merely because it exists.

## Support claims with evidence

Distinguish these evidence levels:

- **Direct observation:** report what a source, measurement, test, or artifact shows.
- **Supported interpretation:** state the narrower conclusion that the evidence supports.
- **Plausible explanation:** label an inference and identify competing explanations when they matter.
- **Unresolved mechanism:** state what the available evidence cannot distinguish and name the missing test.
- **Future work:** describe planned or possible work in future or conditional language.

Attribute scientific and factual claims to their sources. Name benchmark conditions, controls, data splits, and evaluation protocols when they change the interpretation. Keep model scores, predictions, rankings, and generated candidates distinct from experimental confirmation.

Base code claims on repository code, tests, configuration, or current authoritative documentation. Do not call an API deprecated, a method faster, or behavior guaranteed without evidence. Routine code comments do not need citations when the code is sufficient evidence.

If evidence is missing, ask for it, use a placeholder, narrow the statement, or state the uncertainty. Never fill the gap with a plausible invention.

## Use consistent mathematical notation

Apply the same notation in Python, equations, prose, captions, shape comments, and documentation:

- Use lowercase symbols for scalars: `x`, `n`, `d`, `h`, and `p`.
- Use lowercase symbols for vectors: `x`, `q`, and `v`.
- Use bold lowercase vectors in formal mathematical writing when the format permits, such as `\mathbf{x}`.
- Use uppercase symbols for matrices and tensors of rank two or greater: `X`, `W`, `Q`, `K`, and `V`.
- Keep dimension symbols and indices lowercase.
- Update a symbol after a rank change when doing so improves clarity, such as `X` for a matrix and `x` for its reduced vector.
- Apply capitalization to short mathematical symbols only. Keep descriptive Python identifiers in lowercase snake case, such as `hidden_states`, `attention_mask`, and `embedding_vector`.
- Define every nonstandard symbol near its first use and keep it consistent through the full transformation.
- Preserve established external notation, repository conventions, serialized fields, and public APIs when renaming would reduce clarity or change behavior.

For batched data, name the object by its actual rank. A batch of vectors is normally a matrix and therefore takes an uppercase mathematical symbol.

## Choose exact language

- Prefer ordinary verbs and concrete nouns.
- Use one stable term for one concept unless a domain convention requires otherwise.
- Avoid hype, prestige language, vague abstractions, and claims of importance that do not state a consequence.
- Do not use em dashes.
- Preserve exact technical terms, literal interface text, identifiers, commands, paths, quotations, and required external terminology.
- Use American English unless the user or venue requires another convention.
