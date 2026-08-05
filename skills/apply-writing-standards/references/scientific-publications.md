# Scientific publications

Use this profile for manuscripts, preprints, abstracts, introductions, methods, results, discussions, limitations, conclusions, figure captions, and journal responses.

## Core pattern

Name the scientific object, state the result, give the measurement and comparator, explain what the evaluation supports, and bound the interpretation. Keep architecture, training, inference, validation, and biological meaning distinct.

Use strong claims only when the evidence supports them. Treat model outputs as scores, rankings, reconstructions, generations, or priorities unless experimental data confirms the biological claim.

## Abstract

1. State the unresolved scientific or modeling gap.
2. Name the specific method or reframing.
3. State what was built or evaluated.
4. Report key measurements from the source.
5. Bound the interpretation.
6. End with the narrow scientific implication.

## Introduction

Open with the scientific bottleneck. Explain why the strongest relevant approaches leave a data, supervision, leakage, evaluation, scale, modality, or biological ambiguity unresolved. End with the exact test performed and the evidence that would support the claim.

## Methods

Write an audit trail. Name data sources and versions, preprocessing, split logic, controls, inputs, architecture, objective, hardware, randomization, thresholds, metrics, and evaluation protocol. Keep training and validation data, in-distribution and out-of-distribution tests, and model score and biological truth distinct.

## Results

Lead each subsection with the finding. Put measurements immediately after the result, then name the comparator, control, and relevant evaluation condition. Interpret last. Place local caveats beside the result they limit.

## Discussion and conclusion

State the conceptual result and what the controls establish. Identify the study-level limitation that most affects generalization or confidence and state its consequence. Separate what is validated now from what remains possible. End with a specific implication or next experiment, not a generic promise.

## Captions

Make each caption independently useful. State what is shown, the protocol, comparator, split or threshold, and the intended interpretation. Keep identifying information in the caption rather than an embedded figure title when the venue permits.

## Claim language

- Use `shows` for a direct result and `supports` for a bounded conclusion.
- Use `is consistent with` for a compatible explanation.
- Use `we cannot distinguish` when the available test leaves competing explanations.
- Replace `proves` and `solves` with the narrower claim unless a formal proof or complete solution exists.
- Use `state of the art` only with a named benchmark, comparator set, metric, and evaluation condition.
