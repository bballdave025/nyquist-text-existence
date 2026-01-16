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

# Potential Reviewer Questions and Responses (Pre-Registered)

---

---

## ResNet confidence without epistemic info
## Question/Start of Reply Restating Question

> Excellent question. The question was: Did you actually test this against modern vision models, 
>like ResNet, or is this purely theoretical?”

### Clarifications

This question would be in relation to part in the Conclusion/Scope Section


> `"""`

**Model behavior under information loss.**<br/>
We note that modern convolutional vision models may continue to produce confident high-level
classifications (e.g., “document,” “contains text”) even when stroke-scale information is
provably absent at the resolution presented to the model. This behavior reflects the use of
global structure, layout cues, and learned priors rather than access to evidentiary text
signal. Such outputs are therefore not treated here as measurements of text existence.

Instead, they serve to illustrate a potential divergence between model confidence and
information-theoretic availability of evidence once sampling limits are violated. For this
reason, model behavior is discussed only qualitatively and is not used as a primary anchor
or experimental endpoint in this work.

> `"""`

## Answer (at least points)

> That’s an excellent question. We did look at ResNet-style behavior, because it would have been irresponsible not to. What we observed was consistent with the theoretical framing: models can remain confident about document-level or layout-level properties even when the specific textual evidence is no longer present at the resolution they actually receive.
> However, that observation is not what this paper is claiming. The goal here is not to evaluate model performance, but to establish a prior boundary: when sampling removes stroke-scale information, text existence is no longer a well-posed question. Model confidence beyond that point reflects inference around missing information, not access to it.
> For that reason, we intentionally treat model behavior as a secondary illustration rather than a primary experimental anchor.

### Defusing remarks and other ideas

> I would have disappointed my younger, I-want-to-be-a-scientist self if I hadn't at least checked.

---

---

## Talk starter / Prompt Conditioning
## Question: N/A

A coworker with an English Literature background asked me a question about LLMs. I didn’t have a great off-the-cuff answer, but I did know a paper on the topic better than I knew the topic itself, so i told him so. Then, at my suggestion, he asked an LLM to explain the technical ML paper for an Eng Lit guy rather than an ML guy. The response opened with, “Imagine you’re a novelist…,” complete with protagonists and narrative arcs. We laughed, and I suggested he add, “You don’t need to use English Lit terms.” He paused and said, “No — I’ll ask it again, but tell it not to pander to me.”

Ever since, I’ve joked that the real danger sign is when ChatGPT starts using Nyquist metaphors while I’m asking for talking points for my daughter’s bedtime story.

```
(It’s a good reminder that LLMs shine less at answering questions than at helping you work through material you already know is worth reading.)?
```

---

---

### Gathered from lab notebook and chats

**Q1. You invoke the Nyquist limit, but you do not provide a closed-form mathematical definition of the Nyquist boundary for text. Is this a theoretical gap?**

**A1.** No. This work does not claim the existence of a single closed-form Nyquist boundary for text across documents. Stroke-scale writing is shaped by ink diffusion, substrate texture, pen width variability, acquisition optics, bit depth, and compression, which jointly preclude a universal analytic threshold. Instead, we adopt an operational identification of the Nyquist boundary, defined by the joint collapse of multiple observables (e.g., stroke-associated spectral components, edge continuity, and texture convergence). This preserves theoretical honesty while allowing falsifiable evaluation.

---

---

**Q2. Why rely on an operational criterion rather than a purely analytical or information-theoretic proof?**

**A2.** A purely analytical treatment would require idealized assumptions (e.g., band-limited edges, uniform substrates) that do not hold for real manuscript materials. Conversely, a purely empirical threshold would risk post hoc tuning. The operational criterion used here is theory-constrained but measurement-based, reflecting physically meaningful limits without overclaiming mathematical precision.

---

---

**Q3. How do you avoid cherry-picking Image B or its crop to support your claim?**

**A3.** Image B is selected as a pre-registered anchor, not a success case. Its canonical crop is chosen via a deterministic, pre-registered procedure (maximal stroke-energy within a fixed strip along the binding edge). The purpose is not optimality but invariance: once defined, the crop is fixed and not substituted based on outcomes. Alternative crops are treated as distinct analytical objects and are not swapped post hoc.

---

---

**Q4. Why is Image B treated as an illustrative anchor rather than as defining the Nyquist boundary itself?**

**A4.** Image B is used to concretize a theoretically predicted transition under realistic archival digitization conditions. The Nyquist boundary is defined at the level of sampling theory and operational observables, not by any single image. Image B illustrates the boundary; it does not set it.

---

---

**Q5. Modern vision models can still confidently classify images as “text” even when stroke-level detail is lost. Why is this not evidence against your claim?**

**A5.** Such behavior reflects reliance on learned priors, layout regularities, and global structure rather than access to evidentiary stroke-scale signal. This work explicitly distinguishes model confidence from information-theoretic availability of evidence. High confidence in the absence of recoverable signal is treated as a divergence between inference and evidence, not as detection of text existence.

---

---

**Q6. Could human observers outperform machines below the Nyquist boundary?**

**A6.** Humans may appear to outperform machines through perceptual interpolation or contextual inference. However, such judgments do not constitute access to evidentiary signal under this framework. The claim concerns recoverability of signal, not inferential plausibility. Any apparent human advantage below the boundary is therefore out of scope.

---

---

**Q7. How do you define falsification for claims about text existence, rather than recognition or readability?**

**A7.** A claim is falsified if recoverable stroke-scale signal remains detectable below the predicted boundary without the introduction of external information (e.g., priors, generative synthesis, cross-image leakage), and if such detection generalizes across resampling instances. Confidence alone is not sufficient; recoverability of evidentiary signal is required.

---

---

**Q8. Why exclude super-resolution and enhancement methods from confirmatory evidence?**

**A8.** Super-resolution and enhancement introduce information not present in the sampled data. While such methods may produce visually plausible reconstructions, they do not recover original signal and therefore cannot serve as evidence of text existence. Their use is explicitly limited to illustrative, non-confirmatory contexts.

---

---

**Q9. How do you address cases like Herculaneum papyri or multispectral recoveries that appear to “beat” Nyquist limits?**

**A9.** These cases do not contradict the Nyquist boundary as defined here. Successful recovery occurs because the signal existed in the original object and was accessed via additional physical channels or modalities, not because lost sampled information was reconstructed. The boundary distinguishes absence of access from absence of inscription.

---

---

**Q10. Why include cross-script examples (e.g., Japanese diacritics) if the primary anchor is Latin script?**

**A10.** Cross-script examples test the generality of the framework across writing systems with different critical spatial frequencies. The distinction between loss of semantic contrast and loss of text existence proper is expected to vary by script geometry. These examples probe scope, not universality.

---

---

**Q11. The Japanese example is not yet selected. Does this weaken the preregistration?**

**A11.** No. The preregistration constrains the selection criteria and analytical role of the example rather than the specific document. Once selected via addendum, the example will be analyzed regardless of outcome, with no substitution based on results.

---

---

**Q12. Why include fingerprints and surface traces if the focus is text existence?**

**A12.** Fingerprints and non-text traces are explicitly exploratory and serve to sharpen conceptual boundaries between writing, trace, and texture under sampling loss. They do not generate confirmatory claims about text existence and are clearly labeled as such.

---

---

**Q13. Does this work claim that digitization should always occur at maximal resolution?**

**A13.** No. The work does not prescribe archival policy. It characterizes irreversible information loss under sampling and clarifies what can and cannot be claimed once such loss occurs. Practical constraints and trade-offs are acknowledged but not adjudicated.

---

---

**Q14. How does this framework remain compatible with democratized discovery (e.g., work by interns or non-specialists using limited imaging tools)?**

**A14.** The framework clarifies limits rather than imposing exclusivity. Identifying when signal exists—or provably does not—helps guide both high-end imaging strategies and low-resource discovery efforts. In some cases, low-quality digitizations may become the only surviving witnesses, making clarity about evidentiary limits essential rather than elitist.

---

---

**Q15. Why preregister a theory-forward project at all?**

**A15.** Preregistration here serves to lock scope, claims, and falsification criteria, protecting negative results and preventing retrospective boundary-shifting. It is used not to constrain exploration, but to clearly separate confirmatory claims from exploratory insight.

