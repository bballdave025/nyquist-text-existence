# Preregistration — Nyquist Text Existence

**Project:** Nyquist Text Existence

**Provisional Paper Title and Subtitle:**  
**Text Existence at the Nyquist Boundary**  
*Information-Theoretic Limits on Binary Detectability in Digitized Manuscripts*

**Authors:**  
David Black (GitHub @bballdave025)  
Keith Prisbrey (GitHub @keithprisbrey)

**Date of preregistration:** 2026-01-15

**Status:** Pre-experimental (confirmatory phase not yet begun)

---

*Confirmatory analysis begins at the first execution of a pre-registered test on the locked image set and locked resampling procedure.*

---

## 1. Purpose of this preregistration

This preregistration records the core theoretical claims, predictions, and evaluation boundaries of the Nyquist Text Existence project prior to confirmatory experimentation.

The primary goal is to clearly distinguish:

- predictions derived from sampling theory and information-theoretic limits, and  
- exploratory analyses conducted to refine intuition, visualization, or experimental design.

This document is theory-forward. It intentionally avoids commitment to specific model architectures, training regimes, enhancement pipelines, or optimization procedures. Its purpose is to define what can be claimed—and falsified—about text existence under sampling constraints, independent of recognition or interpretation.

---

## 2. Scope of claims

### 2.1 Text Existence

This preregistration concerns **text existence**, defined as:

> The presence or absence of recoverable signal corresponding to writing in a digitized image, independent of recognition, transcription, or interpretation.

Recoverable signal refers to inscription-specific evidentiary information, not merely visible stroke geometry, segmentable structure, coarse layout regularities, or global form.

The scope explicitly excludes:

- OCR accuracy,  
- semantic correctness,  
- paleographic interpretation,  
- historical attribution,  
- or claims about authorial intent.

The focus is strictly on whether evidentiary signal corresponding to writing exists in the sampled image data.

### 2.2 Scale dependence and non-transitivity

Text existence is not a transitive or scale-invariant property of image regions. A region that is part of a larger text-bearing structure may itself contain no text-evidentiary signal at a given spatial scale.

Accordingly, NTEC is explicitly scale-relative and does not assert transitivity of text existence across regions or resolutions.

### 2.3 Model behavior under information loss

Modern vision models may continue to produce confident high-level classifications (e.g., “document,” “contains text”) even when inscription-specific evidentiary signal is provably absent at the resolution presented to the model. Such behavior reflects reliance on global structure, layout cues, and learned priors rather than access to recoverable text signal.

Model confidence is therefore not treated here as a measurement of text existence. Model behavior is discussed only qualitatively to illustrate potential divergence between confidence and information-theoretic availability of evidence once sampling limits are violated.

---

## 3. Primary theoretical claim

### 3.1. Claim 1 (Nyquist Text Existence)

If stroke-scale spatial frequencies or intensity gradients corresponding to writing fall below the Nyquist limit imposed by sampling resolution, bit depth, or compression, then the signal corresponding to text ceases to exist in the digitized image.

Once this loss occurs, no downstream method—human, neural, or generative—can recover evidentiary signal corresponding to original inscription, as distinct from inferred or synthesized structure.

This claim concerns the existence of signal, not the performance of recognition systems.

---

## 4. Operational identification and derived predictions

### 4.1. Operational identification of the Nyquist boundary

Operationally, the Nyquist Text Existence Criterion (NTEC) identifies the boundary at which stroke-level writing signal becomes unrecoverable under downsampling. The boundary is treated as an operational transition characterized by the joint collapse of multiple observables, including:

- loss of stroke-associated spectral components,  
- failure of edge-based representations to preserve stroke continuity, and  
- convergence of text-bearing regions toward texture-like statistics under further downsampling.

The boundary is considered crossed when these observables jointly indicate that stroke-level signal is no longer recoverable under any invertible transformation of the sampled data.

Exact thresholds depend on ink–substrate contrast, stroke width variability, edge smoothness, acquisition optics, and bit depth. These factors preclude a single closed-form boundary while still permitting consistent operational identification across images.

### 4.2. Derived predictions

From Claim 1, we preregister the following predictions.

#### 4.2.1. Prediction 1: Abrupt failure under downsampling

There exists a sampling threshold below which text existence transitions from recoverable to undecidable, and this transition is abrupt rather than gradual.

Failure below this threshold reflects information-theoretic loss, not model inadequacy or insufficient training.

**Falsification criterion:**  
This prediction would be falsified if recoverable stroke-scale signal remains detectable below the nominal Nyquist threshold without the introduction of external information (e.g., priors, generative synthesis, or cross-image leakage).

---

#### 4.2.2. Prediction 2: Model-agnostic failure

Below the sampling threshold, diverse model classes (e.g., CNNs, vision transformers, VLMs) will fail to identify text existence in qualitatively similar ways, despite architectural or training differences.

Any retained confidence reflects priors, layout cues, or global structure rather than access to stroke-level evidentiary signal.

**Falsification criterion:**  
This prediction would be falsified if one or more model classes reliably identify text existence below the threshold using only the degraded image data, and this identification generalizes across images and resampling instances.

---

#### 4.2.3. Prediction 3: Human–machine parity after signal loss

Once sampling destroys stroke-scale information, human observers will not reliably outperform machine systems in determining text existence, except via contextual inference or perceptual interpolation.

Such inference does not constitute access to evidentiary signal and is not treated as evidence of text existence under this framework.

**Falsification criterion:**  
This prediction would be falsified if humans reliably identify text existence below the sampling threshold using only the degraded image data, in a manner that generalizes across observers and images and cannot be attributed to contextual or prior-driven inference.

---

## 5. Image-specific anchor case (Image B)

### 5.1. Role of Image B

Image B is designated as a pre-registered **anchor case** illustrating the Nyquist Text Existence boundary under realistic archival digitization conditions. It is not selected as a success case.

The anchor instantiates a theoretically predicted transition between:

- recoverable stroke-scale writing signal, and  
- undecidable texture following routine resampling.

### 5.2. Canonical crop selection

We define a **canonical crop**[^2] as the specific region of Image B evaluated under NTEC.

To avoid outcome-dependent selection, we preregister a deterministic crop-selection procedure. Candidate horizontal strips near the upper binding edge are evaluated using a sliding-window edge-strength measure that quantifies the concentration of high-contrast, stroke-like transitions. The strip maximizing this measure is selected. In the event of a tie, the strip with the smallest horizontal coordinate in the original image orientation is chosen.

The exact crop boundaries, expressed as pixel coordinates relative to Image B (canonical), will be recorded prior to any resampling, enhancement, or visualization and treated as fixed for all confirmatory analyses.

The purpose of defining a canonical crop is not to privilege a particular region as optimal, but to prevent outcome-driven substitution among plausible alternatives.

### 5.3. Pre-registered expectations for Image B

1. At native resolution, stroke-scale structure corresponding to writing is recoverable.  
2. Under routine downsampling or compression consistent with common archival workflows, the same region becomes undecidable with respect to text existence.  
3. The transition is attributable to sampling decisions alone and persists across observers and model classes.

**Falsification criterion:**  
These expectations would be falsified if stroke-scale writing signal remains recoverable below the predicted threshold without the introduction of external information, or if apparent recovery depends on enhancement methods that introduce new information rather than preserve sampled signal.

### 5.4. Image B provenance and usage

Image B is drawn from the FamilySearch digital collection *“Sweden, Malmöhus Church Records, 1541–1918,”* originating from microfilm of archival material held by Landsarkivet i Lund (Sweden) and digitized under standard archival imaging practices.

Citation:  
“Sweden, Malmöhus, Church Records, 1541–1918,” images, FamilySearch (https://www.familysearch.org : accessed 2026-01-14), Domkapitlet i Lund > A III Protokoll (domböcker) i äktenskapsmål > vol. 4, 1646–1649, image 5 of 111; Landsarkivet i Lund (Sweden Regional Archives, Lund).

Usage complies with FamilySearch access and citation guidelines; see Note [3].

---

## 6. Cross-script extension (Japanese diacritic challenge)

### 6.1 Semantic Distinction and Text Existence Thresholds 

We preregister the expectation that writing systems with small, information-critical diacritics (e.g., Japanese dakuten / handakuten) violate sampling limits at different thresholds than Latin scripts.

In cross-script contexts, we distinguish between two related but non-identical limits:

1. loss of semantic distinction within a writing system, and  
2. loss of text existence proper, defined as the presence of recoverable writing signal at all.

Semantic distinctions carried by diacritics are expected to be lost before full base-glyph structure collapses. Depending on script geometry and stroke distribution, text existence may persist after semantic distinction fails or may collapse simultaneously.

Recoverable signal refers to inscription-specific evidentiary information, not merely visible stroke geometry or segmentable structure.

### 6.2 Analytical role and boundary structure

This extension probes whether multiple Nyquist-style boundaries may occur within a single writing system:

- a **semantic boundary**, at which diacritic-scale information becomes unrecoverable and semantic distinctions collapse, and  
- an **existence boundary**, at which recoverable writing signal ceases to exist entirely.

These boundaries need not coincide. A region may retain base-glyph structure after semantic distinctions are lost, or may lose all stroke-scale signal simultaneously.

The predicted ordering — semantic collapse preceding or coinciding with existence collapse — constitutes an empirical claim about the geometry of information loss in multi-scale writing systems.

### 6.3 Planned cross-script example

At the time of preregistration, the specific Japanese document has not been selected. Instead, we preregister the selection criteria and analytical role of this example.

The Japanese example will satisfy the following constraints:

- semantic distinction depends on diacritic-scale marks,  
- the base glyph remains invariant,  
- the diacritic occupies a small spatial footprint relative to the glyph, and  
- the document is a real historical or genealogical record.

The example is not treated as an additional anchor case. Once specified via addendum, it will be analyzed regardless of outcome.

### 6.4 Judgment protocol

Semantic distinguishability will be evaluated by an expert or native reader of Japanese.

Judges will assess, under degraded sampling alone and without enhancement or contextual priors, whether the semantic distinction encoded by the diacritic remains recoverable. Judgments concern semantic discriminability, not visual salience or stylistic plausibility.

OCR systems will not be used as evaluators.

### 6.5 Falsification criterion

**Falsification criterion:**  
This extension is falsified if diacritic-scale semantic distinctions remain reliably recoverable at sampling regimes where base-glyph stroke structure has already crossed the NTEC existence boundary, or if no separable semantic boundary is observed prior to complete collapse of recoverable writing signal.

Such an outcome would falsify the predicted ordering of semantic and existence boundaries in this cross-script case.

Failure of this prediction does not falsify the Nyquist Text Existence Criterion itself. It would instead delimit the geometry of information loss across writing systems and indicate that semantic and existence boundaries may coincide or invert under certain stroke distributions.

### 6.6 Scope of inference

This cross-script analysis does not assert that semantic collapse implies text non-existence, nor that semantic preservation implies recoverability of evidentiary signal. It serves solely to characterize the relative ordering of semantic and existence boundaries under controlled sampling loss and to test whether multi-scale collapse behavior generalizes across scripts.

---

## 7. Diagnostic boundary and positive-complement investigation

### 7.1. Motivation and diagnostic question

A central motivation of the positive-complement investigation is not merely to identify cases of recoverable text, but to characterize the boundary between regions of an image that can be said to contain plausible text signal and regions that cannot, given only the sampled data. While the Nyquist Text Existence Criterion (NTEC) is formulated primarily as a loss condition — identifying when recoverable text signal must cease to exist under sampling — the complementary question is whether there exists a principled diagnostic for asserting that a given image region plausibly contains text signal at all, prior to any attempted reconstruction or enhancement.

Such a diagnostic would not aim to recover text, but to assess whether the hypothesis “this region contains text signal” is logically supportable from the sampled data alone. NTEC is an asymmetrical criterion: it can rule out the existence of recoverable text signal under a specified sampling regime, but failure to rule it out does not constitute evidence that such signal exists.

### 7.2. Exploratory procedure

To explore this boundary, we propose an exploratory procedure operating on known success cases in which text was later recovered through physical or imaging methods (e.g., bindings, burned text, shadowed text, palimpsests), but where only the original digitized images are available to the analyst. For each document, regions will be sampled using sliding windows at multiple scales. For each region, we compute frequency-domain and stroke-energy descriptors derived from the local Fourier spectrum and spatial gradients, and compare these to corresponding descriptors from visibly legible text elsewhere in the same document. Regions that later proved to contain text (according to independent recovery) will be contrasted with visually similar regions that did not. The primary outcome is not classification accuracy, but whether regions later confirmed to contain text occupy a distinct distributional neighborhood in descriptor space prior to recovery.

### 7.3. Diagnostic hypothesis

This procedure tests the diagnostic hypothesis that regions later confirmed to contain text will, prior to recovery, exhibit descriptor distributions that differ measurably from those of visually similar non-text regions drawn from the same document.

### 7.4. Falsification criterion

**Falsification criterion:**  
This hypothesis is falsified if regions later confirmed to contain text are statistically indistinguishable from visually similar non-text regions under all examined descriptors, scales, and sampling conditions. Such a result constitutes a negative finding, indicating that the sampled data contains no diagnostically usable evidence of text existence prior to recovery.

This negative outcome is an intended and informative result. It would strengthen the claim that the text existence boundary is sharp and that successful post-hoc recovery methods operate beyond what the original samples can justify.

### 7.5. Role of NTEC as a necessary-condition filter

Under this framework, NTEC functions as a necessary-condition filter on claims of text existence. When sampling constraints provably eliminate recoverable stroke-scale signal at the relevant spatial scale, asserting even the possibility of text existence in that region is not epistemically justified on the basis of the sampled data. In such cases, recovery attempts may produce visually plausible reconstructions, but these cannot be supported as evidentiary claims about original inscription.

Conversely, when NTEC does not rule out recoverable signal, this does not establish text existence, but it preserves the logical permissibility of further physical or imaging investigation. NTEC thus forbids certain claims outright while remaining deliberately agnostic in cases where information-theoretic constraints do not preclude recoverability.

### 7.6. Scope of inference and scale-relative non-transitivity

Crucially, this procedure is not intended as a reconstruction method, nor as a detection algorithm, but as a diagnostic probe of signal plausibility near the existence boundary. A positive result would indicate that, even when text is not visually legible, sampled images may contain measurable signatures consistent with “just-above-threshold” text signal. A negative result would be equally informative, indicating that such regions are indistinguishable from non-text prior to recovery.

A region that is part of a larger text-bearing structure may itself contain no text-evidentiary signal at a given spatial scale. NTEC is explicitly scale-relative and does not assert transitivity of text existence across scales or regions.

Failure of this specific diagnostic procedure does not falsify the general role of NTEC as a necessary-condition filter on claims of text existence. It would instead delimit the practical detectability of pre-recovery signatures within the descriptor families examined here.

### 7.7. Epistemic triage

This diagnostic framing allows NTEC to be used not only as a criterion for irreversible loss, but also as a tool for epistemic triage: identifying which regions merit further physical or imaging investigation and which do not, based solely on the information present in the sampled data. Importantly, any claims arising from this analysis are restricted to plausibility of signal existence, not to content recovery or interpretation. This maintains a strict separation between existence, detectability, and reconstruction, and provides a principled framework for deciding when recovery efforts are theoretically supported by the data and when they are not.

---

## 8. Fingerprints and non-text surface traces (explicitly exploratory)

### 8.1 NTEC intuition: Nyquist existence for non-text objects

This project includes exploratory analysis of fingerprints and related non-text surface traces frequently observed in manuscript imagery.

These analyses are intended to clarify similarities and differences between writing signals and non-text ridge-based or texture-based structures under sampling loss, and to refine conceptual boundaries between inscription, trace, and texture.

### 8.2 Fingerprints as a contrast class

Fingerprints exhibit highly regular ridge–valley structure with comparatively narrow frequency bands and strong orientation coherence. This regularity is expected to make fingerprint signals particularly sensitive to sampling loss.

Once contrast is sufficiently degraded, the only remnants of fingerprint structure are expected to be:

- gross shape constraints imposed by the contact region,  
- anisotropic smearing or directional remnants in the image or spectrum, or  
- geometric distortion of an originally coherent ridge field.

Such remnants preserve little or no evidentiary value for identifying a region as a fingerprint, and substantially less for identification of the fingerprint itself.

Crucially, these remnants may preserve segmentable structure or visible geometry without preserving inscription- or trace-specific evidentiary signal.

### 8.3 Scale dependence and loss of evidentiary value

As with text, fingerprint existence is scale-relative and non-transitive across regions.

A region that is part of a larger fingerprint-bearing structure may itself contain no fingerprint-evidentiary signal at a given spatial scale, even while retaining geometric continuity or shape constraints.

Recoverable signal here refers to ridge–valley alternation carrying identification-relevant information, not merely the presence of elongated or banded texture.

### 8.4 Exploratory hypothesis

We hypothesize that fingerprint signals will exhibit **earlier and more abrupt catastrophic collapse** under downsampling than writing signals, due to:

- narrower and more regular frequency bands,  
- stronger orientation coherence, and  
- reduced redundancy across spatial scales.

Under this hypothesis, fingerprints are expected to lose evidentiary ridge information at higher resolutions than text loses stroke information, leaving behind only non-evidentiary shape or smear remnants.

### 8.5 Falsification criterion

**Falsification criterion:**  
This exploratory hypothesis would be falsified if fingerprint-bearing regions retain stable, ridge-specific evidentiary signal across downsampling regimes in which stroke-scale writing signal has already collapsed, in a manner that generalizes across documents and acquisition conditions.

### 8.6 Role in the project

Fingerprint analyses do not generate confirmatory claims about text existence. They are used to:

- contrast collapse behavior between inscription and non-inscription signals,  
- clarify the distinction between separability and recoverability, and  
- refine the conceptual boundary between evidentiary signal and residual structure.

These analyses are explicitly exploratory and are not treated as anchors or primary theoretical tests. Fingerprint analyses do not generate confirmatory claims about text existence and are explicitly labeled as exploratory.

---

## 9. Role of super-resolution and enhancement

Super-resolution and enhancement methods may generate visually plausible reconstructions below the Nyquist limit.

Such outputs introduce information and are not treated as evidence of original inscription. Increased confidence based on such reconstructions does not imply recoverability of signal.

Region selection and downsampling procedures will be locked prior to any generative reconstruction. Super-resolution outputs may be shown illustratively but are not used to support confirmatory claims.

---

## 10. Confirmatory vs. exploratory analyses

### 10.1. Confirmatory analyses

- Tests of preregistered predictions  
- Conducted under locked image regions and locked resampling procedures  
- Evaluated against preregistered falsification criteria  

### 10.2. Exploratory analyses

- Visualization choices  
- Model selection  
- Enhancement techniques  
- Qualitative inspection, including fingerprints and surface traces  

Exploratory analyses are expected and explicitly labeled.

### 10.3. Edge cases and non-goals

Humans and models may infer “text exists” from global regularities even when stroke-scale evidence is absent. Such inferences lie outside the stroke-existence criterion analyzed here and are treated as future work.

---

## 11. Deviations and addenda

Any deviation from this preregistration will be documented as an addendum. Addenda may refine scope or introduce new hypotheses but will not retroactively alter preregistered claims or evaluation criteria.

---

## 12. Intended use

This preregistration is intended to support transparent collaboration, protect negative results, and serve as a stable reference for workshops, arXiv preprints, and related discussion.

It does not assert priority, ownership, or completeness.

---

## 13. Notes

[1] Real writing signals are band-limited by physical factors such as pen width, ink diffusion, substrate texture, and acquisition optics. The Nyquist boundary here concerns loss of physically meaningful stroke information, not elimination of all high-frequency components.

[2] *Canonical* denotes the unique, fixed data object designated for evaluation under NTEC. Canonical does not imply optimality or standardization; it reflects commitment to a single, explicitly defined evidentiary object chosen via a preregistered procedure.

[3] Image B corresponds to FamilySearch DGS 004534287, image 00361.

---

*End of preregistration.*
