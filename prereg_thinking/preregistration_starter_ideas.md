# Preregistration — Nyquist Text Existence

**Project:** Nyquist Text Existence  

**_Provisional Paper Title and Subtitle:_**  

**Text Existence at the Nyquist Boundary**  
*Information-Theoretic Limits on Binary Detectability in Digitized Manuscripts*

**Authors:**  
David Black (GitHub @bballdave025)  
Keith Prisbrey (GitHub @keithprisbrey)

**Date of preregistration:** ((Goal 2026-01-21, almost certainly to OSF))

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

This preregistration concerns **text existence**, defined as:

> The presence or absence of recoverable signal corresponding to writing in a digitized image, independent of recognition, transcription, or interpretation.

The scope explicitly excludes:

- OCR accuracy,  
- semantic correctness,  
- paleographic interpretation,  
- historical attribution,  
- or claims about authorial intent.

The focus is strictly on whether evidentiary signal corresponding to writing exists in the sampled image data.

### Model behavior under information loss

Modern vision models may continue to produce confident high-level classifications (e.g., “document,” “contains text”) even when stroke-scale information is provably absent at the resolution presented to the model. Such behavior reflects reliance on global structure, layout cues, and learned priors rather than access to evidentiary text signal.

Accordingly, model confidence is not treated here as a measurement of text existence. Model behavior is discussed only qualitatively to illustrate potential divergence between confidence and information-theoretic availability of evidence once sampling limits are violated. Models are not used as primary anchors or experimental endpoints in this work.

---

## 3. Primary theoretical claim

### Claim 1 (Nyquist Text Existence)

If stroke-scale spatial frequencies or intensity gradients corresponding to writing fall below the Nyquist limit imposed by sampling resolution, bit depth, or compression, then the signal corresponding to text ceases to exist in the digitized image.

Once this loss occurs, no downstream method—human, neural, or generative—can recover evidentiary signal corresponding to original inscription, as distinct from inferred or synthesized structure.

This claim concerns the existence of signal, not the performance of recognition systems.

---

## 4. Operational identification and derived predictions

### Operational identification of the Nyquist boundary

Operationally, the Nyquist Text Existence Criterion (NTEC) identifies the boundary at which stroke-level writing signal becomes unrecoverable under downsampling. The boundary is treated as an operational transition characterized by the joint collapse of multiple observables, including:

- loss of stroke-associated spectral components<sup>[1]</sup>,  
- failure of edge-based representations to preserve stroke continuity, and  
- convergence of text-bearing regions toward texture-like statistics under further downsampling.

The boundary is considered crossed when these observables jointly indicate that stroke-level signal is no longer recoverable under any invertible transformation of the sampled data.

Exact thresholds depend on ink–substrate contrast, stroke width variability, edge smoothness, acquisition optics, and bit depth. These factors preclude a single closed-form boundary while still permitting consistent operational identification across images.

### Derived predictions

From Claim 1, we preregister the following predictions.

#### Prediction 1: Abrupt failure under downsampling

There exists a sampling threshold below which text existence transitions from recoverable to undecidable, and this transition is abrupt rather than gradual.

Failure below this threshold reflects information-theoretic loss, not model inadequacy or insufficient training.

**Falsification criterion:**  
This prediction would be falsified if recoverable stroke-scale signal remains detectable below the nominal Nyquist threshold without the introduction of external information (e.g., priors, generative synthesis, or cross-image leakage).

---

#### Prediction 2: Model-agnostic failure

Below the sampling threshold, diverse model classes (e.g., CNNs, vision transformers, VLMs) will fail to identify text existence in qualitatively similar ways, despite architectural or training differences.

Any retained confidence reflects priors, layout cues, or global structure rather than access to stroke-level evidentiary signal.

**Falsification criterion:**  
This prediction would be falsified if one or more model classes reliably identify text existence below the threshold using only the degraded image data, and this identification generalizes across images and resampling instances.

---

#### Prediction 3: Human–machine parity after signal loss

Once sampling destroys stroke-scale information, human observers will not reliably outperform machine systems in determining text existence, except via contextual inference or perceptual interpolation.

Such inference does not constitute access to evidentiary signal and is not treated as evidence of text existence under this framework.

**Falsification criterion:**  
This prediction would be falsified if humans reliably identify text existence below the sampling threshold using only the degraded image data, in a manner that generalizes across observers and images and cannot be attributed to contextual or prior-driven inference.

---

## 5. Image-specific anchor case (Image B)

### Role of Image B

Image B is designated as a pre-registered **anchor case** illustrating the Nyquist Text Existence boundary under realistic archival digitization conditions. It is not selected as a success case.

The anchor instantiates a theoretically predicted transition between:

- recoverable stroke-scale writing signal, and  
- undecidable texture following routine resampling.

### Canonical crop selection

We define a **canonical crop**<sup>[2]</sup> as the specific region of Image B evaluated under NTEC.

To avoid outcome-dependent selection, we preregister a deterministic crop-selection procedure. Candidate horizontal strips near the upper binding edge are evaluated using a sliding-window edge-strength measure that quantifies the concentration of high-contrast, stroke-like transitions. The strip maximizing this measure is selected. In the event of a tie, the strip with the smallest horizontal coordinate in the original image orientation is chosen.

The exact crop boundaries, expressed as pixel coordinates relative to Image B (canonical), will be recorded prior to any resampling, enhancement, or visualization and treated as fixed for all confirmatory analyses.

The purpose of defining a canonical crop is not to privilege a particular region as optimal, but to prevent outcome-driven substitution among plausible alternatives.

### Pre-registered expectations for Image B

1. At native resolution, stroke-scale structure corresponding to writing is recoverable.  
2. Under routine downsampling or compression consistent with common archival workflows, the same region becomes undecidable with respect to text existence.  
3. The transition is attributable to sampling decisions alone and persists across observers and model classes.

**Falsification criterion:**  
These expectations would be falsified if stroke-scale writing signal remains recoverable below the predicted threshold without the introduction of external information, or if apparent recovery depends on enhancement methods that introduce new information rather than preserve sampled signal.

### Image B provenance and usage

Image B is drawn from the FamilySearch digital collection *“Sweden, Malmöhus Church Records, 1541–1918,”* originating from microfilm of archival material held by Landsarkivet i Lund (Sweden) and digitized under standard archival imaging practices.

Citation:  
“Sweden, Malmöhus, Church Records, 1541–1918,” images, FamilySearch (https://www.familysearch.org : accessed 2026-01-14), Domkapitlet i Lund > A III Protokoll (domböcker) i äktenskapsmål > vol. 4, 1646–1649, image 5 of 111; Landsarkivet i Lund (Sweden Regional Archives, Lund).

Usage complies with FamilySearch access and citation guidelines; see Note [3].

---

## 6. Cross-script extension (Japanese diacritic challenge)

We preregister the expectation that writing systems with small, information-critical diacritics (e.g., Japanese dakuten / handakuten) violate sampling limits at different thresholds than Latin scripts.

In cross-script contexts, we distinguish between two related but non-identical limits:

1. loss of semantic distinction within a writing system, and  
2. loss of text existence proper, defined as the presence of recoverable writing signal at all.

Semantic distinctions carried by diacritics are expected to be lost before full base-glyph structure collapses. Depending on script geometry and stroke distribution, text existence may persist after semantic distinction fails or may collapse simultaneously.

### Planned cross-script example

At the time of preregistration, the specific Japanese document has not been selected. Instead, we preregister the selection criteria and analytical role of this example.

The Japanese example will satisfy the following constraints:

- semantic distinction depends on diacritic-scale marks,  
- the base glyph remains invariant,  
- the diacritic occupies a small spatial footprint relative to the glyph, and  
- the document is a real historical or genealogical record.

The example is not treated as an additional anchor case. Once specified via addendum, it will be analyzed regardless of outcome. OCR will not be used; assessment will rely on stroke-scale signal behavior under controlled resampling.

---

## 7. Fingerprints and non-text surface traces (explicitly exploratory)

This project includes exploratory analysis of fingerprints and related non-text surface traces frequently observed in manuscript imagery.

These analyses are intended to clarify similarities and differences between text and non-text signals under sampling loss and to refine conceptual boundaries between writing, trace, and texture.

Fingerprint analyses do not generate confirmatory claims about text existence and are explicitly labeled as exploratory.

---

## 8. Role of super-resolution and enhancement

Super-resolution and enhancement methods may generate visually plausible reconstructions below the Nyquist limit.

Such outputs introduce information and are not treated as evidence of original inscription. Increased confidence based on such reconstructions does not imply recoverability of signal.

Region selection and downsampling procedures will be locked prior to any generative reconstruction. Super-resolution outputs may be shown illustratively but are not used to support confirmatory claims.

---

## 9. Confirmatory vs. exploratory analyses

### Confirmatory analyses

- Tests of preregistered predictions  
- Conducted under locked image regions and locked resampling procedures  
- Evaluated against preregistered falsification criteria  

### Exploratory analyses

- Visualization choices  
- Model selection  
- Enhancement techniques  
- Qualitative inspection, including fingerprints and surface traces  

Exploratory analyses are expected and explicitly labeled.

### Edge cases and non-goals

Humans and models may infer “text exists” from global regularities even when stroke-scale evidence is absent. Such inferences lie outside the stroke-existence criterion analyzed here and are treated as future work.

---

## 10. Deviations and addenda

Any deviation from this preregistration will be documented as an addendum. Addenda may refine scope or introduce new hypotheses but will not retroactively alter preregistered claims or evaluation criteria.

---

## 11. Intended use

This preregistration is intended to support transparent collaboration, protect negative results, and serve as a stable reference for workshops, arXiv preprints, and related discussion.

It does not assert priority, ownership, or completeness.

---

## 12. Notes

[1] Real writing signals are band-limited by physical factors such as pen width, ink diffusion, substrate texture, and acquisition optics. The Nyquist boundary here concerns loss of physically meaningful stroke information, not elimination of all high-frequency components.

[2] *Canonical* denotes the unique, fixed data object designated for evaluation under NTEC. Canonical does not imply optimality or standardization; it reflects commitment to a single, explicitly defined evidentiary object chosen via a preregistered procedure.

[3] Image B corresponds to FamilySearch DGS 004534287, image 00361.

---

*End of preregistration.*
