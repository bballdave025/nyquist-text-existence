# Preregistration — Nyquist Text Existence

**Project:** Nyquist Text Existence

**Provisional Paper Title and Subtitle:**

Text Existence at the Nyquist Boundary

_Information-Theoretic Limits on Binary Detectability in Digitized Manuscripts_

**Authors:**

David Black (GitHub @bballdave025)

Keith Prisbrey (GitHub @keithprisbrey)

**Date of preregistration:** 2026-01-13

**Status:** Pre-experimental (confirmatory phase not yet begun)

---

_Confirmatory analysis begins at the first execution of a pre-registered test on the locked image set and locked resampling procedure._

---

## 1. Purpose of this preregistration

This preregistration records the core theoretical claims, predictions, and evaluation boundaries of the Nyquist Text Existence project prior to confirmatory experimentation.

The primary goal is to clearly distinguish:

- predictions derived from sampling theory and information-theoretic limits, and
- exploratory analyses conducted to refine intuition, visualization, or experimental design.

This document is theory-forward. It intentionally avoids commitment to specific model architectures, training regimes, enhancement pipelines, or optimization procedures.

---

## 2. Scope of claims

This preregistration concerns **text existence detection**, defined as:

> The presence or absence of recoverable signal corresponding to writing in a digitized image, independent of recognition, transcription, or interpretation.

The scope explicitly excludes:

- OCR accuracy,
- semantic correctness,
- paleographic interpretation,
- historical attribution,
- or claims about authorial intent.

The focus is strictly on whether evidentiary signal corresponding to writing exists in the sampled image data.

---

## 3. Primary theoretical claim

### Claim 1 (Nyquist Text Existence)

If stroke-scale spatial frequencies or intensity gradients corresponding to writing fall below the Nyquist limit imposed by sampling resolution, bit depth, or compression, then the signal corresponding to text ceases to exist in the digitized image.

Operationally, the Nyquist boundary is identified when a majority of stroke-associated spectral components collapse below a pre-specified detectability criterion under downsampling.

In this work, the Nyquist boundary is treated as an operational transition characterized by simultaneous collapse of multiple observables, including:

- loss of stroke-associated spectral components,
- failure of edge-based representations to preserve stroke continuity,
- and convergence of text-bearing regions toward texture-like statistics under further downsampling.

The boundary is considered crossed when these observables jointly indicate that stroke-level signal is no longer recoverable under any invertible transformation of the sampled data.

While idealized bitonal edges exhibit arbitrarily high spatial frequencies, real writing signals are band-limited by physical factors such as pen width, ink diffusion, substrate texture, and acquisition optics. The Nyquist boundary relevant here concerns the loss of physically meaningful stroke information, not the elimination of all high-frequency components.

Exact thresholds depend on ink–substrate contrast, stroke width variability, edge smoothness, and bit depth. These factors preclude a single closed-form boundary while still permitting consistent operational ((CG. Right word? detection)).

Once this loss occurs, no downstream method—human, neural, or generative—can recover evidentiary signal corresponding to original inscription, as distinct from inferred or synthesized structure.

---

## 4. Derived predictions

From Claim 1, we pre-register the following predictions.

### Prediction 1: Abrupt failure under downsampling

There exists a sampling threshold below which text existence transitions from recoverable to undecidable, and this transition is abrupt rather than gradual.

Failure to detect text below this threshold reflects information-theoretic loss, not model inadequacy or insufficient training.

**Falsification criterion:**

This prediction would be falsified if recoverable stroke-scale signal remains detectable below the nominal Nyquist threshold without the introduction of external information (e.g., priors, generative synthesis, or cross-image leakage).

---

### Prediction 2: Model-agnostic failure

Below the sampling threshold, diverse model classes (e.g., CNNs, vision transformers, VLMs) will fail to detect text existence in qualitatively similar ways, despite architectural or training differences.

Any retained confidence reflects priors, layout cues, or global structure, not access to stroke-level evidentiary signal.

**Falsification criterion:**

This prediction would be falsified if one or more model classes reliably detect text existence below the threshold using only the degraded image data, and this detection generalizes across images and resampling instances.

---

### Prediction 3: Human–machine parity after signal loss

Once sampling destroys stroke-scale information, human observers will not reliably outperform machine systems in determining text existence, except via perceptual interpolation or contextual inference.

Such inference does not constitute access to evidentiary signal and is not treated as evidence of text existence under this framework.

Any apparent human advantage below the sampling threshold is expected to derive from contextual inference or perceptual interpolation rather than access to evidentiary signal. Such advantage does not constitute evidence of text existence under this framework. (CG. Keep? No comment is being made about the value of such advantage.)

---

## 5. Image-specific anchor (Image B)

Image B is designated as a pre-registered anchor case illustrating the Nyquist Text Existence boundary under realistic archival digitization conditions.

### Role of Image B

Image B is not selected as a success case. It serves to instantiate a theoretically predicted transition between:
- recoverable stroke-scale writing signal, and
- undecidable texture following routine resampling.

### Pre-registered expectations

For Image B:

1. At native resolution, stroke-scale structure corresponding to writing is recoverable.
2. Under routine downsampling or compression consistent with common archival (CG, Keep? and Computer Vision) workflows, the same region becomes undecidable with respect to text existence.
3. The transition is attributable to sampling decisions alone and persists across model classes and human observers.

### Falsification criterion

This anchor expectation would be falsified if:

- stroke-scale writing signal remains recoverable after resampling below the predicted threshold without the introduction of external information, or
- recovery depends on enhancement methods that introduce new information rather than preserve sampled signal.

Image B is used to concretize the Nyquist boundary, not to define it.

### Image B provenance (summary):

Image B is drawn from the FamilySearch digital collection “Sweden, Malmöhus Church Records, 1541–1918,” specifically a digitized court record volume (Domkapitlet i Lund, A III Protokoll, domböcker i äktenskapsmål). The image originates from microfilm of archival material held by Landsarkivet i Lund (Sweden) and was digitized by FamilySearch under standard archival imaging practices.

### Image B Citation and Usage

“Sweden, Malmöhus, Church Records, 1541–1918,” images, FamilySearch (https://www.familysearch.org : accessed 2026-01-14), Domkapitlet i Lund > A III Protokoll (domböcker) i äktenskapsmål > vol. 4, 1646–1649, image 5 of 111; Landsarkivet i Lund (Sweden Regional Archives, Lund).

For access information, see Note \[3\].



---

## 6. Cross-script extension (Japanese diacritic challenge)

We pre-register the expectation that writing systems with small, information-critical diacritics (e.g., Japanese dakuten / handakuten) violate sampling limits at different thresholds than Latin scripts.

### Prediction:

In cross-script contexts, we distinguish between two related but non-identical limits: (i) loss of semantic distinction within a writing system, and (ii) loss of text existence proper, defined as the presence of recoverable writing signal at all.

- Semantic distinctions carried by diacritics are expected to be lost before full base glyph structure collapses.
- Depending on script geometry and stroke distribution, text existence may persist after semantic distinction fails, or may collapse simultaneously with base glyph structure.

This extension is intended to test generality across writing systems without asserting universality.

---

## 7. Fingerprints and non-text surface traces (explicitly exploratory)

This project includes **exploratory but serious analysis** of fingerprints and related non-text surface traces frequently observed in manuscript imagery.

These analyses are intended to:

- clarify similarities and differences between text and non-text signals under sampling loss,
- test whether Nyquist-based collapse applies consistently to other fine-grained, human-produced surface structures,
- and refine conceptual boundaries between “writing,” “trace,” and “texture.”

Fingerprint analyses are **not** treated as primary anchors and do not generate confirmatory claims about text existence. They are used to sharpen intuition, contrast signal geometries, and contextualize the text-specific results.

All such analyses will be explicitly labeled as exploratory.

No confirmatory claims about text existence are derived from these analyses.

---

## 8. Role of super-resolution and enhancement

Super-resolution and enhancement methods may generate visually plausible reconstructions below the Nyquist limit.

### Pre-registered position:

- Such outputs introduce information.
- They are not treated as evidence of original inscription.
- Increased human or model confidence based on such reconstructions does not imply recoverability of signal.

Super-resolution results may be shown illustratively but are not used to support confirmatory claims.

---

## 9. Confirmatory vs. exploratory analyses

### Confirmatory analyses

- Tests of the predictions listed above
- Conducted under locked image regions and locked resampling procedures
- Evaluated against pre-registered criteria

### Exploratory analyses

- Visualization choices
- Model selection
- Enhancement techniques
- Qualitative inspection (including fingerprints and surface traces)

Exploratory work is allowed and expected, but will be explicitly labeled as such and separated from confirmatory results.

---

## 10. Deviations and addenda

Any deviation from this preregistration will be documented as an addendum, not a replacement.

Addenda may clarify scope, refine predictions, or introduce new hypotheses, but will not retroactively alter pre-registered claims or evaluation criteria.

---

## 11. Intended use

This preregistration is intended to:

- support transparent collaboration,
- protect negative results,
- and serve as a stable reference for workshops, arXiv preprints, and related discussion.

It does not assert priority, ownership, or completeness.

---

## 12. Notes

3. Image B corresponds to FamilySearch DGS 004534287, image 00361.

---

*End of preregistration.*
