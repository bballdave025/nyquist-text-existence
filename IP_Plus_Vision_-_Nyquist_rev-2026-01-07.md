# IP_Plus_Vision — Nyquist Text Existence

**Project:** Nyquist Text Existence  
**Author:** David Black (DWB)  
**Status:** Vision + technical framing (theory-forward; experiments forthcoming)  
**Relationship:** Companion methodology to RMFB and related manuscript-imagery projects

---

## 0. What this document is

This document defines the **conceptual scope, theoretical claims, and experimental framing** for the *Nyquist Text Existence* project.

It is intended to:
- formalize a set of **pre-registered, falsifiable claims**,
- clarify **information-theoretic limits** that precede model choice,
- and provide a stable citation anchor for future experimental and applied work.

This is a *vision-plus-theory* document, not a report of completed experiments.

---

## 0.1 Arrival notes (how to read this)

This project proceeds from a deliberately conservative stance:

- When information has been destroyed by sampling, **it does not exist** in the digitized image.
- No model—neural, symbolic, or hybrid—can recover information that was never sampled.
- Failures are therefore not always *model failures*; many are *acquisition failures*.

Negative results are expected and are treated as informative.

---

## 0.2 Explicit non-goals

This project does **not** aim to:

- propose new OCR or handwriting-recognition systems;
- outperform existing text-recognition benchmarks;
- recover information beyond physical sampling limits;
- introduce proprietary digitization, compression, or imaging methods;
- treat hallucinated reconstructions as historical evidence.

Super-resolution, enhancement, and generative models may be discussed, but only as **illustrative contrasts**, not as recovery mechanisms.

---

## 1. Core claim (high level)

Many failures of text and surface-trace detection in digitized manuscript imagery are governed not by model limitations or training data scarcity, but by **fundamental constraints imposed by sampling theory**.

When digitization, preprocessing, or compression decisions eliminate critical spatial or intensity information, the corresponding signal ceases to exist within the image itself. No downstream model can recover information that has been destroyed at acquisition or encoding time.

---

## 2. Text existence ≠ text recognition

A central distinction of this work is between:

- **Text existence detection**  
  (Is there evidence that writing is present at all?)

and

- **Text recognition**  
  (What characters or symbols are present?)

These problems operate at **different sampling thresholds**.

A system may fail to detect the presence of writing entirely, even though the same text would be legible to humans in a higher-resolution or higher-bit-depth representation of the same artifact.

We do not measure readability; we establish the conditions under which readability is even theoretically possible.

---

## 3. Directional frequency structure of text

Text is not an isotropic visual phenomenon.

Across many historical scripts, writing exhibits:

- **High-frequency structure orthogonal to stroke direction**  
  (ink–blank–ink alternation at stroke width and inter-stroke gaps)

- **Lower-frequency structure along writing direction**  
  (baselines, ascenders/descenders, line spacing)

Detectability of text presence depends primarily on preservation of the **highest-frequency components**, which are often much finer than those required to identify page layout or material texture.

---

## 4. Nyquist limits and irreversible loss

When spatial sampling falls below twice the dominant stroke-scale frequency:

- Under proper anti-aliasing, those components are removed;
- Under naive downsampling, they are aliased into unrelated frequencies.

In either case, the original ink–substrate signal no longer exists.

This is not degradation but **annihilation**.

Below the Nyquist limit, text presence is not merely difficult to infer—it is **undecidable** from the available data.

---

## 5. Bit depth as a second Nyquist-like constraint

Spatial resolution is not the only axis along which information is lost.

**Intensity quantization introduces an independent constraint.**

In many reused or degraded manuscript contexts:
- ink contrast occupies only a small fraction of the available dynamic range;
- faint strokes, offsets, or fingerprints rely on subtle gradients.

Low bit-depth capture (e.g., 8-bit grayscale):
- collapses those gradients into quantization noise;
- suppresses edge responses used by CNNs and transformer models.

Even when spatial sampling satisfies Nyquist criteria, insufficient intensity resolution can render textual signals undetectable.

---

## 6. Humans vs. machines (why intuition misleads)

Humans:
- integrate context across space,
- apply strong priors about letterforms,
- tolerate heavy quantization by perceptual interpolation.

Machines:
- operate on local gradients,
- cannot assume intent,
- cannot reconstruct gradients that were never sampled.

This is not a flaw of machine learning; it is a consequence of upstream sampling decisions.

---

## 7. JPEG compression as a Nyquist interaction (experimental motivation)

JPEG compression is optimized for **human visual salience**, not for preserving fine edge gradients.

Even at high quality settings:
- block-based transforms,
- quantization of high-frequency coefficients,
- and chroma subsampling

can suppress stroke-scale information.

### Pre-registered experimental question *(for Keith)*

> Does JPEG compression at fixed spatial resolution reduce recoverable stroke-frequency or gradient information below Nyquist thresholds for text and surface traces that remain detectable in PNG/TIFF representations?

This is a testable acquisition-level hypothesis, not a claim about JPEG’s design intent.

---

## 8. Script dependence and generality

The Nyquist argument is **script-agnostic**, but critical frequencies differ by writing system.

- Latin scripts often concentrate high frequencies orthogonal to stroke direction.
- CJKV scripts exhibit dense, two-dimensional stroke structure.

As a result, some scripts may violate sampling limits **more rapidly** under downsampling or quantization.

This work treats script variation as a parameter, not an exception.

---

## 9. Extension beyond text: surface traces and material signals

The sampling constraints described here apply not only to text, but to other
fine-scale, high-frequency visual phenomena common in manuscript imagery,
including:

- fingerprints and palm prints,
- sewing and stitching traces,
- tooling marks and abrasion patterns,
- surface preparation artifacts,
- follicle patterns in animal skin.

These features often occupy spatial frequency regimes comparable to or higher
than those of small handwriting strokes. When their defining structure is lost
through downsampling, compression, or quantization, the phenomenon ceases to
exist as a classifiable signal within the image.

In this project, non-textual classifications are assigned only when defining
structural features are explicitly present in the digitized image itself.
Suggestive marks or expert inference without structural support are excluded.

This conservative stance prioritizes evidentiary clarity over completeness and
preserves a clear separation between **evidence** and **interpretation**.

---

## 10. Pre-registered, falsifiable claims *(for Keith)*

The following claims are specified **prior to experimentation**. Each includes
explicit refutation criteria.

### H1 — Spatial Nyquist (text existence)

If stroke-scale spatial frequencies fall below the Nyquist limit due to
downsampling, text existence becomes undecidable for both humans and models.

**Refutation:** Demonstration of reliable text existence detection from images
provably sampled below the Nyquist threshold without introducing new
information.

---

### H2 — Bit-depth quantization

At fixed spatial resolution, reduced intensity bit depth suppresses gradients
required for text and surface-trace detection.

**Refutation:** Demonstration that low-bit-depth captures preserve equivalent
gradient information and detection performance for low-contrast traces.

---

### H3 — JPEG interaction

At fixed spatial resolution, JPEG compression disproportionately degrades
recoverable stroke-scale information relative to lossless formats.

**Refutation:** No measurable difference in recoverable high-frequency or
gradient information between JPEG and lossless encodings under controlled
conditions.

---

### H4 — Human–machine parity under signal annihilation

Once sampling removes critical stroke-scale information, humans do not
outperform models in detecting text existence.

**Refutation:** Reliable human detection of text existence where no model
operating on the same sampled image succeeds.

---

### H5 — Script-dependent critical frequencies

Scripts with dense, two-dimensional stroke structure reach Nyquist violation
under downsampling or quantization at higher resolutions than scripts with
predominantly directional strokes.

**Refutation:** Equivalent sampling thresholds across scripts with
substantially different stroke density and orientation.

---

## 11. Discussion

\[Simply a placeholder for now.\]

## 11. Conclusion and scope boundary

This project formalizes a simple but often neglected point: **digitization
choices determine which historical signals remain available for computation at
all**.

When information has been destroyed by sampling, no amount of model
sophistication can recover it. Treating such absences as model failures
misdirects effort and obscures the true limiting factors.

By grounding text and surface-trace detection in sampling theory, this work
provides:
- a principled basis for abstention,
- a rationale for full-resolution and multi-scale analysis,
- and a framework for evaluating negative results without post hoc revision.

**Model behavior under information loss.**

We note that modern convolutional vision models may continue to produce confident high-level classifications (e.g., “document,” “contains text”) even when stroke-scale information is provably absent at the resolution presented to the model. This behavior reflects the use of global structure, layout cues, and learned priors rather than access to evidentiary text signal. Such outputs are therefore not treated here as measurements of text existence. Instead, they serve to illustrate a potential divergence between model confidence and information-theoretic availability of evidence once sampling limits are violated. For this reason, model behavior is discussed only qualitatively and is not used as a primary anchor or experimental endpoint in this work.

This document establishes theory and scope. Experiments will test—not extend—
these claims.
