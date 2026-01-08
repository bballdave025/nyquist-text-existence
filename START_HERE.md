# Start Here — Nyquist Text Existence

## Welcome, Keith!

This repository explores the **information-theoretic limits of text existence detection** in digitized manuscript imagery.  
It is theory-forward, experiment-ready, and intended to support clean, falsifiable testing rather than post hoc interpretation.

If you are arriving fresh (especially as a collaborator), ... Ahem, there's some formality from ChatGPT, Keith, this is for you: the order below is recommended.

---

## Suggested Reading Order

### 1. Thematic Image Anchor (start here)
**`thematic_image_info.md`**

You can choose a glance at the thematic image before, during, or after your reading, i.e look at the [image being discussed in that document](https://raw.githubusercontent.com/bballdave025/nyquist-text-existence/refs/heads/ready-for-keith/draft_figures/FamilySearch_-_DGS004534287_00361.jpg) from that link to the left, or look at it and illustrative zooms in the [draft_images](draft_images) directory.

This document introduces **Image B**, the low–pixel-footprint binding text that motivated the Nyquist framing, and explains why it recurs throughout the project.

- Focus: *intuition + grounding*
- Key ideas:
  - text existence vs. text recognition,
  - pixel-faithful evidence vs. interpolation,
  - why some signals are provably unrecoverable.

The **CJKV diacritic challenge** (for you, Keith : ) is included near the end as a concrete cross-script extension. (**I dare you, Keith.*")

> Draft zooms and illustrative crops of Image B are located in  
> [**`./draft_figures/`**](draft_figures) (for presentation and intuition only; experiments should resample from originals).

---

### 2. Vision and Technical Framing
**`IP_Plus_Vision_-_Nyquist_Text_Existence.md`**

This is the core conceptual document.

- Focus: *claims, scope, and experimental motivation*
- Defines:
  - pre-registered, falsifiable claims,
  - Nyquist limits (spatial + bit depth),
  - JPEG compression as an acquisition-level hypothesis,
  - script dependence as a parameter, not an exception.

Experiments are explicitly marked as forthcoming. (Forthcoming until you run them 😎)

---

### 3. Figures, Drafts, and Experimental Scaffolding
**`./draft_figures/`**  
**(and future experiment directories)**

Contains:
- draft crops and zooms for Image B,
- exploratory visual material,
- placeholders for future experimental results.

These materials are **illustrative unless explicitly labeled otherwise**.

---

## How to Engage

There is no required path forward.

Possible next steps include:
- proposing or running controlled sampling experiments,
- identifying parallel examples (e.g., CJKV diacritics),
- stress-testing the claims with counterexamples,
- or refining acquisition-level hypotheses.

Questions, critiques, and alternative framings are welcome.

---

## Project Stance (one paragraph summary)

When sampling decisions eliminate critical spatial or intensity information, the corresponding signal does not exist in the digitized image.  
No downstream model—human or machine—can recover what was never sampled.  
This project treats negative results and abstention as principled outcomes, not failures.

---

*Thank you for taking a look.*
