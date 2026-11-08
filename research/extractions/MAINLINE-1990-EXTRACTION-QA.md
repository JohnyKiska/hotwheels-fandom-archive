# Mainline 1990: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1990/List of 1990 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `f3106ca0de09c4e9d8f626b55aeb772fee6c3923`
- File size: 441,532 bytes (Git tree size)
- Manifest SHA-256: `d0a8fc18f706e9324f777b1051a08f3fec01194add33ce699c2f89e522cd83e2`
- Fandom revision: 754020

Machine-readable export: [MAINLINE-1990.csv](MAINLINE-1990.csv). All source fields, table boundaries, and raw headers/cells are preserved.

## Extraction method

Extracted four product tables and 87 rows. New Castings has 12 columns and a Collector # field. Reissues, The Simpsons and California Customs have 11/11/9 columns respectively and no Collector # field.

## QA results

| Check | Result |
|---|---:|
| Product tables | 4 |
| Source rows | 87 |
| New Castings | 8 |
| Reissues | 50 |
| The Simpsons | 2 |
| California Customs | 27 |
| Unique Col # values | 8 |
| Unique nonblank Toy # values | 66 |
| Blank Toy # rows | 8 |
| Repeated Toy # groups | 11 |
| Rows with Col # field | 8 |
| Rows without Col # field by schema | 79 |

Repeated Toy # values:
- 1238: 2 rows
- 1241: 3 rows
- 1287: 2 rows
- 1289: 2 rows
- 1296: 2 rows
- 1299: 3 rows
- 1301: 2 rows
- 1303: 2 rows
- 3371: 2 rows
- 5128: 2 rows
- 9580: 2 rows

## Table inventory

- Table 1, New Castings [ ]: 8 rows; 12 columns (Col # | Casting Name | Series | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo)
- Table 2, Reissues [ ]: 50 rows; 11 columns (Casting Name | Series | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo)
- Table 3, The Simpsons [ ]: 2 rows; 11 columns (Casting Name | Series | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo)
- Table 4, California Customs [ ]: 27 rows; 9 columns (Casting Name | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Photo)

## Interpretation notes

- Only New Castings has a Collector # column (8 rows). Do not infer Collector # for Reissues, The Simpsons or California Customs.
- Eight Reissues rows have blank Toy #: Baja Bug, GT Racer, Rescue Ranger (two rows), Tough Customer, CAT Road Roller, CAT Dump Truck and Bywayman.
- Reissues has no Collector # column. California Customs and The Simpsons are separate lists with no Collector #.
- Repeated Toy # values are source-level collisions across castings, color variants and sections; Toy # is not a universal unique release key.
- The page contains a distinct The Simpsons licensed section (2 rows) and California Customs (27 rows). Preserve section provenance.
- Fandom is a secondary source; verify missing Toy # and identifier collisions with packaging/catalogues before normalization.
