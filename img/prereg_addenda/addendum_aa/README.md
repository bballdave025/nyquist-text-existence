# Addendum AA Figure Assets

This directory contains image assets used in **Addendum AA** of the preregistration follow-up materials.

Addendum AA is an exploratory module centered on the **Smallest Distinguishable Feature** framing introduced in collaboration discussions with Keith Prisbrey.

It explores how practical feature-size limits relate to the broader Nyquist Text Existence Criterion (NTEC), especially as a useful first-pass or leading-order approximation.

---

# Addendum AA Working Theme

A central motivating idea is that many recoverability questions are initially governed by whether the smallest relevant writing feature is sampled with sufficient effective resolution to remain distinguishable.

Informally:

$$
\text{recoverability} \;\approx\; f(\text{feature scale}, \text{sampling scale})
$$

and, as a leading-order intuition,

$$
f_{\mathrm{NTEC}}(\mathcal{M}) = f_0 + \mathcal{O}(\text{higher-order effects})
$$

where the dominant first term may often be approximated by Nyquist / sampling constraints.

This does **not** exhaust the full NTEC framework, but it provides an intuitive and practically valuable entry point.

---

# Purpose of This Folder

This folder exists so that image assets may be merged to `main` early and referenced by stable links in:

- OSF addenda
- GitHub markdown documents
- pull requests
- notes and lab notebooks
- collaborator drafts

Text documents may continue evolving on feature branches while figures remain stable here.

---

# Current Figure Inventory

## `smallest_feature_slide.png`

Cleaned reference image derived from Keith Prisbrey’s presentation slide:

> **Feature size is not just one pixel**

The figure illustrates two complementary ideas:

1. empirical distribution of smallest distinguishable feature sizes across a dataset
2. marked example region showing a smallest distinguishable feature in context

It is especially relevant because it connects formal sampling language to practical recognizability in real genealogical record imagery.

This figure serves as the initial anchor image for Addendum AA.

---

# Scientific Role of These Figures

Figures in this directory may be used to illustrate:

- feature-scale limits
- distinguishability thresholds
- sampling adequacy
- pixels-per-stroke intuition
- practical scanner / sensor constraints
- the bridge between engineering heuristics and formal NTEC theory

---

# Design Philosophy

This folder is intended to remain:

- lightweight
- stable
- collaborator-friendly
- citation-ready
- expandable as Addendum AA matures

---

# Status

This directory may contain both provisional and publication-ready assets during active development.
