# Mainline 1985: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1985/List of 1985 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `11b87d7dd43cf89478c2cdf4cbc93f631cf2407d`
- File size: 391,394 bytes
- Manifest SHA-256: `a67eb83f17bb2dcc8558d0a64041d85a263d71ee31c2fc4fb6f564ea782a1096`
- Fandom revision: 765060

Machine-readable export: [MAINLINE-1985.csv](MAINLINE-1985.csv). The export preserves table index, section heading, row position, source column count, source headers, all source cell values, and the mapped descriptive fields. Empty Toy # values remain empty; they are not inferred.

## Extraction method

Extracted all four product tables and 38 source rows. Navigation/footer table excluded. Source table order and row order are retained.

## QA results

| Check | Result |
|---|---:|
| Product tables | 4 |
| Source rows | 38 |
| Unique nonblank Toy # | 27 |
| Blank Toy # | 11 |
| Source rows with all descriptive fields preserved | 38 |
| Collector # column | Not present |
| Series # column | Not present |
| Photo cells empty | 38 / 38 |

## Table inventory

- Table 1: New Castings [ ]: 4 rows; 12 source columns
- Table 2: Real Riders [ ]: 7 rows; 12 source columns
- Table 3: Ultra Hots [ ]: 8 rows; 11 source columns
- Table 4: Reissues [ ]: 19 rows; 12 source columns

## Notable source features and unresolved points

- The New Castings and Reissues tables use 12-column schemas, including a Series column that is blank in many or all rows. Ultra Hots uses an 11-column schema and has no Series column.
- No Collector # or Series # field appears in these 1985 tables. Do not synthesize either identifier from row order or Toy #.
- Reissues include multiple variants of the same casting, including two Baja Bug rows and two Neet Streeter rows. These are separate source rows and must remain separate.
- Turbo Streak appears in both Real Riders and Reissues, with different wheel-type labels and source context. Do not collapse these rows by casting name.
- Toy # is blank for several Real Riders/Reissues entries. Blank values remain blank.
- The source includes historical notes such as “originally issued as …”, pack-only appearance, and playset appearance. These are source assertions and should be retained as notes, not treated as independently verified casting lineage.
- Exact name matches do not prove the same physical release, tooling, or package. Fandom remains a secondary source.

## Table schemas

- Table 1 (New Castings [ ]): Casting Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 2 (Real Riders [ ]): Casting Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 3 (Ultra Hots [ ]): Casting Name | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 4 (Reissues [ ]): Casting Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
