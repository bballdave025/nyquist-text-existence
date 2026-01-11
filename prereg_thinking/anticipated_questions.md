# Anticipated Questions and Scope Clarifications
## Nyquist Text Existence Project

## Purpose of this document

This document records questions, objections, and points of clarification that
the authors anticipate may arise from readers, reviewers, collaborators, or
conference audiences.

Its purpose is **not** to introduce new claims, results, or hypotheses.
Instead, it serves to:

- clarify project scope before experimentation,
- distinguish conceptual boundaries from empirical claims,
- document decisions made *prior* to preregistered analysis,
- and reduce the risk of post-hoc rationalization or scope drift.

This document is part of the **preregistration thinking layer** of the project
and is intentionally separate from both the paper draft and the preregistered
analysis plan.

---

## Status and intended use

- This document is **internal-facing** and may evolve.
- It is intended to support collaboration and preregistration hygiene.
- Content here may inform—but will not be copied verbatim into—the final paper
  or preregistration submission.

Questions recorded here may later be:
- answered experimentally,
- addressed explicitly in the paper,
- or ruled out of scope by design.

---

## Relationship to preregistration

Anticipating questions is treated as a *methodological safeguard*, not as
argumentation.

Where relevant, this document helps ensure that:
- hypotheses are defined before data analysis,
- exclusions and scope limits are principled rather than reactive,
- and confirmatory analysis begins only after procedures are locked.

No analysis decisions are made in this document.

---

## Relationship to IP_Plus_Vision

The IP_Plus_Vision document defines the **conceptual and theoretical framing**
of the project.

This document exists downstream of that framing and upstream of formal
preregistration. It addresses how the framing is likely to be interpreted,
challenged, or misunderstood, without modifying the framing itself.


---

## Question/Start of Reply Restating Question

> Excellent question. The question was: Did you actually test this against modern vision models, 
>like ResNet, or is this purely theoretical?”

### Clarifications

This question would be in relation to part in the Conclusion/Scope Section

> **Model behavior under information loss.**<br/>
> We note that modern convolutional vision models may continue to produce confident high-level
> classifications (e.g., “document,” “contains text”) even when stroke-scale information is
> provably absent at the resolution presented to the model. This behavior reflects the use of
> global structure, layout cues, and learned priors rather than access to evidentiary text
> signal. Such outputs are therefore not treated here as measurements of text existence.
> Instead, they serve to illustrate a potential divergence between model confidence and
> information-theoretic availability of evidence once sampling limits are violated. For this
> reason, model behavior is discussed only qualitatively and is not used as a primary anchor
> or experimental endpoint in this work.

## Answer (at least points)

> That’s an excellent question. We did look at ResNet-style behavior, because it would have been irresponsible not to. What we observed was consistent with the theoretical framing: models can remain confident about document-level or layout-level properties even when the specific textual evidence is no longer present at the resolution they actually receive.
> However, that observation is not what this paper is claiming. The goal here is not to evaluate model performance, but to establish a prior boundary: when sampling removes stroke-scale information, text existence is no longer a well-posed question. Model confidence beyond that point reflects inference around missing information, not access to it.
> For that reason, we intentionally treat model behavior as a secondary illustration rather than a primary experimental anchor.

### Defusing remarks and other ideas

> I would have disappointed my younger, I-want-to-be-a-scientist self if I hadn't at least checked.
