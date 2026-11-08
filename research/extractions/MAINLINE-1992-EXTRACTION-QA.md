# Mainline 1992: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1992/List of 1992 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `571c5840c9ae38a314eb7bd6a430ac0b84998a48`
- File size: 373,227 bytes (Git tree size)
- Manifest SHA-256: `9b9d04e6cc75b8a9164872578d9ab258fda26d3684ae5af7993a0942d9ff780e`
- Fandom revision: 783535

Machine-readable export: [MAINLINE-1992.csv](MAINLINE-1992.csv). All source columns, table boundaries and row positions are preserved. The 1992 page contains two 12-column tables and one 9-column Gleam Team table.

## Extraction method

Extracted all 3 product tables and 24 source rows. Field mapping is by header name; no assumption that every table shares the same schema.

## QA results

| Check | Result |
|---|---:|
| Product tables | 3 |
| Source rows | 24 |
| New Castings | 12 |
| Reissues | 7 |
| Gleam Team | 5 |
| Distinct nonblank Col # | 24 |
| Distinct nonblank Toy # | 22 |
| Blank Toy # rows | 2 |
| Duplicate Col # values | 0 |
| Duplicate Toy # values | 0 |

## Table inventory

- Table 1, New Castings [ ]: 12 rows; 12 columns (Col # | Car name | Series | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo)
- Table 2, Reissues [ ]: 7 rows; 12 columns (Col # | Car name | Series | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo)
- Table 3, Gleam Team [ ]: 5 rows; 9 columns (Col # | Car Name | Color | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Photo)

## Interpretation notes

- New Castings and Reissues use a 12-column release-detail schema; Gleam Team uses a 9-column schema and has no Series/Tampo/Notes columns.
- Gleam Team Col #189 (Gleamer Patrol) and #190 ('57 T-Bird) have blank Toy # values in the source. Preserve blanks; do not infer Toy # from adjacent entries.
- Toy # values such as `0773` and `0444` contain leading zeroes. Store identifiers as text, not integers.
- Collector # and Toy # are distinct identifiers.
- The archived Fandom page does not independently establish release status or casting/tooling identity. Verify missing Toy # values against packaging/catalogues before normalization.
