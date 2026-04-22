# Addendum 2 Figure Assets

This directory contains image assets used in **Addendum 2** of the preregistration follow-up materials.

Addendum 2 introduces and illustrates the measurement-dependent and region-dependent formulation:

$$ \mathrm{NTEC}(M, R) $$

where:

- $\mathrm{M}$ = a specific measurement / capture instance  
- $\mathrm{R}$ = a specific region within that measurement

The figures in this directory are intended to provide concrete visual examples of non-invariance across measurements and regions.

---

# Purpose of This Folder

This folder exists so that image assets may be merged to `main` early and referenced by stable links in:

- OSF addenda
- GitHub markdown documents
- pull requests
- notes and lab notebooks

Text drafts may continue evolving on feature branches while figures remain stable here.

---

# Filename Convention

Files use the following schema:

```text
[source]_[phenom]_[M####]_[R_*]_[status].png
```

### Example

```text
fs8835608_tbrrgt_M0706_R04_unofficialcrop.png
fs8105019_inkovr_M1921_R02_officialcrop.png
```

---

# Field Definitions

| Field | Meaning | Example |
|---|---|---|
| `source` | Source collection / institution / DGS / shelfmark identifier | `fs8835608` |
| `phenom` | Short phenomenon-family code (max 7 chars) | `tbrrgt`, `inkovr` |
| `M#####` | Measurement identifier (usually image number) | `M0706`, `M1921` |
| `R_*` | Region identifier | `R_overview`, `R_big`, `R04` |
| `status` | Crop / curation state | `unofficialcrop`, `officialcrop` |

---

# Region Codes

| Code | Meaning |
|---|---|
| `R_overview` | Broad contextual image / whole page |
| `R_big` | Main selected phenomenon region |
| `R01`, `R02`, ... | Indexed subregions within the main region |

---

# Phenomenon Codes

| Code | Meaning |
|---|---|
| `inkovr` | Ink spill / heavy over-inking obscuration example |
| `tbrrgt` | Right-edge ribbon of readable background reuse |

Additional phenomenon codes may be added as needed.

---

# Important Notes

- `M#####` identifies distinct captures; it does **not** imply identical scanner or lighting conditions across files.
- Region labels make explicit the region-dependent nature of analysis.
- `unofficialcrop` denotes exploratory working crops.
- `officialcrop` denotes finalized publication-ready crops.

---

# Design Philosophy

The naming system is intentionally:

- compact
- sortable
- human-readable
- script-friendly
- stable under project growth

It is meant to support rapid retrieval without embedding excessive prose in filenames.

---

# Status

This folder may contain both finalized and exploratory figure assets during active development.
