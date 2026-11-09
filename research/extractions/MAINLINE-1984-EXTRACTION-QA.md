# Mainline 1984: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1984/List of 1984 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `79ebdf25757fb841eb74a4c2ec3233ddd80a315d`
- File size: 388,718 bytes
- Manifest SHA-256: `1967f24aa259c7b3f54988e8acac15730c8e92e6781905429426ab7c128daf52`

Machine-readable export: [MAINLINE-1984.csv](MAINLINE-1984.csv). The export preserves source table index, section heading, row position, original headers and every source cell. Blank Toy # values are retained.

## Extraction method

Extracted all four product tables and 35 source rows. Navigation/footer table excluded. Source table order and row order are retained.

## QA results

| Check | Result |
|---|---:|
| Product tables | 4 |
| Source rows | 35 |
| Unique nonblank Toy # | 25 |
| Blank Toy # | 4 |
| Repeated Toy # groups | 6 |
| Repeated casting-name groups | 7 |
| Collector # column | Not present |
| Series # column | Not present |
| Photo cells empty | 35 / 35 |

## Table inventory

- Table 1: New Castings [ ]: 14 rows; 12 source columns
- Table 2: Real Riders [ ]: 9 rows; 12 source columns
- Table 3: Ultra Hots [ ]: 8 rows; 11 source columns
- Table 4: Reissues [ ]: 4 rows; 12 source columns

## Repeated Toy # values

- Toy # 3290: Rolls-Royce Phantom II (New Castings [ ], row 9); Rolls-Royce Phantom II (New Castings [ ], row 10)
- Toy # 4372: Lightning Gold (Real Riders [ ], row 7); Lightning Gold (Real Riders [ ], row 8)
- Toy # 4921: Troop Convoy (New Castings [ ], row 12); Troop Carrier (New Castings [ ], row 13)
- Toy # 5902: Sol-Aire CX-4 (Ultra Hots [ ], row 5); Sol-Aire CX-4 (Ultra Hots [ ], row 6)
- Toy # 5909: Dream Van XGW (Real Riders [ ], row 5); Dream Van XGW (Real Riders [ ], row 6)
- Toy # 7293: Flame Runner (Ultra Hots [ ], row 1); Flame Runner (Ultra Hots [ ], row 2)

## Interpretation notes

- New Castings and Reissues use 12-column schemas; Ultra Hots uses 11 columns and has no Series field.
- No Collector # or Series # is present. Do not infer identifiers from row order.
- Real Riders includes repeated casting names and blank Toy # values; keep each source row distinct.
- Ultra Hots includes two Flame Runner rows with the same Toy # 7293 but different Color values (Spectraflame Gold and Unpainted). This is a repeated Toy # group, not grounds for automatic row collapse.
- The Wind Splitter row notes a Malaysia version in addition to its Hong Kong entry. The note does not provide a second independently described row.
- Source notes such as “New casting”, “Originally released as …” and “Same casting as …” are retained as assertions from Fandom, not independently verified tooling/release relationships.
- Exact name or Toy # matches do not establish identical physical releases or tooling.

## Table schemas

- Table 1 (New Castings [ ]): Car Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 2 (Real Riders [ ]): Car Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 3 (Ultra Hots [ ]): Car Name | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 4 (Reissues [ ]): Car Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
