## Filename Schema for Addendum Figures

To support reproducibility, rapid lookup, and consistent reference across images, crops, and exploratory examples, figures use a structured filename schema.

### General Pattern

```text
[source]_[phenom]_[M#####]_[R_*]_[status].png
```

### Fields

| Field | Meaning | Example |
|---|---|---|
| `source` | Collection / shelfmark / DGS identifier | `fs8835608` |
| `phenom` | Short phenomenon code (max 7 chars) | `tbrrgt` |
| `M#####` | Measurement identifier | `M0706` |
| `R_*` | Region identifier | `R_overview`, `R04` |
| `status` | Crop state | `unofficialcrop` |

### Examples

```text
fs8835608_tbrrgt_M0706_R_overview_unofficialcrop.png
fs8835608_tbrrgt_M0706_R04_unofficialcrop.png
fs8105019_inkovr_M1921_R02_officialcrop.png
```
