# Mainline 1995: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1995/List of 1995 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `cfc54031a991a745512b22345fc772f75c78d0cd`
- File size: 456,340 bytes (Git tree size)
- Manifest SHA-256: `ae9f2cdac7f242681115034af43e6626af792dcfdcc417f784bb24924106ec10`
- Fandom revision: 797722

Machine-readable export: [MAINLINE-1995.csv](MAINLINE-1995.csv). It preserves source table index, section heading, row position, source column count, all source headers and values. The 7-column 1995 Hot Wheels table has separate Color and Rims fields; these are explicitly mapped and retained.

## Extraction method

Extracted all 15 product tables and 97 source rows. Navigation/footer tables are excluded. Table order and row order are preserved.

## QA results

| Check | Result |
|---|---:|
| Product tables | 15 |
| Source rows | 97 |
| Unique Toy # | 97 |
| Unique Collector # | 97 |
| Collector # values | 005, 028, 031, 035, 044, 076, 117, 135, 147, 162, 164, 200, 201, 207, 227 ... 355, 356, 357, 358, 359, 360, 361, 362, 363, 364 |
| Rows in 1995 Hot Wheels table | 25 |
| Source table with Color/Rims columns | 1 |
| Treasure Hunt rows | 12 |
| Series # values with zero-width Unicode | 72 |
| Exact repeated Collector # groups | 0 |
| Photo cells empty | 86 |

## Table inventory

- Table 1, 1995 Model Series [ ]: 12 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 2, 1995 Treasure Hunts [ ]: 12 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 3, Race Team Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 4, Krackle Car Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 5, Steel Stamp Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 6, Pearl Driver Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 7, Dark Rider Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 8, Roarin' Rods Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 9, Hot Hubs Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 10, Speed Gleamer Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 11, "Real Riders" Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 12, Silver Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 13, Photo Finish Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 14, Racing Metals Series [ ]: 4 rows; 6 columns (Toy # | Col.# | Model Name | Series | Series # | Photo)
- Table 15, 1995 Hot Wheels [ ]: 25 rows; 7 columns (Toy # | Col. # | Model Name | Color | Rims | Series | Photo)

## Interpretation notes

- Collector # values are sparse across the annual page and are not a dense 001–250 sequence. Preserve source identifiers; do not infer missing products from unrepresented numbers.
- The 1995 Hot Wheels table has seven columns: Toy #, Collector #, Model Name, Color, Rims, Series, Photo. Color and Rims are source attributes, not separate series or casting identities.
- 72 Series # values contain zero-width Unicode. Preserve raw strings and normalize only in derived fields.
- Treasure Hunts are a separate annual section with their own Series # 1/12–12/12; keep Series # and Collector # as distinct fields.
- The archived Fandom page is a secondary source and does not independently establish Mattel release status or casting/tooling identity.
