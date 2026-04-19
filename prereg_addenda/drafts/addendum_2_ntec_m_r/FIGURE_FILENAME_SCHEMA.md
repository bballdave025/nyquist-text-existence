## Filename Schema for Addendum Figures

To support reproducibility, rapid lookup, and consistent reference across images, crops, and exploratory examples, figures use a structured filename schema.

### General Pattern

```text
[source]_[phenom]_[M#####]_[R_*]_[status].png
```

### Fields

| Field | Meaning | Example |
|---|---|---|
| `source` | Collection / shelfmark / DGS identifier | `fs008835608` |
| `phenom` | Short phenomenon code (max 7 chars) | `tbrrgt` |
| `M#####` | Measurement identifier | `M00706` |
| `R_*` | Region identifier | `R_overview`, `R04` |
| `status` | Crop state | `unofficialcrop` |

### Examples

```text
fs008835608_tbrrgt_M00706_R_overview_unofficialcrop.png
fs008835608_tbrrgt_M00706_R04_unofficialcrop.png
fs008105019_inkovr_M01921_R02_officialcrop.png
```

### Design Goals

This schema is intended to:
- preserve provenance of each image
- distinguish recurring phenomenon families
- support direct reference to $\mathrm{NTEC}\left(M, R\right)$ examples
- enable alphabetical grouping and rapid retrieval
- remain human-readable without excessive filename length

## Notes

- `phenom` codes are intentionally short and stable once assigned. They may contain a maximum of seven characters.
- Measurement identifiers need not imply identical lighting or scanner conditions; they denote distinct captures.
- Region identifiers make explicit the region-dependent nature of analysis.
- Official publication figures may use `officialcrop`; exploratory working figures should use `unofficialcrop`.
