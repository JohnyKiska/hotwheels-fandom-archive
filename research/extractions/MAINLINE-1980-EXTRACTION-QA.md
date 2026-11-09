# Mainline 1980: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1980/List of 1980 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `d1646eb99627d5b589b3ed1ffbc6ddd611891a0c`
- File size from Git tree: 405,994 bytes
- Manifest SHA-256: `be56b179a2a44f22e0f75a77fa1f76a24f3519e4cbeb9fdc6a077e7f9a2db81d`
- Fandom revision: 809492

Machine-readable export: [MAINLINE-1980.csv](MAINLINE-1980.csv). The export preserves source table index, section heading, row position, original headers and every source cell. Blank Toy # values are retained.

## Extraction method

Extracted 2 product tables and 49 source rows in source order. Navigation/footer table excluded.

## QA results

| Check | Result |
|---|---:|
| Product tables | 2 |
| Source rows | 49 |
| Unique nonblank Toy # | 42 |
| Blank Toy # | 3 |
| Repeated Toy # groups | 4 |
| Repeated casting-name groups | 3 |
| Collector # column | Not present |
| Series # column | Not present |
| Photo cells empty | 49 / 49 |

## Table inventory

- Table 1: New Castings [ ]: 19 rows; 11 source columns
- Table 2: Reissue and New Colors [ ]: 30 rows; 11 source columns
- Table 3: Hot Wheels by Year [ ]: 1 rows; 1 source columns (navigation/footer)

## Repeated Toy # values

- **2014**: Hot Bird (Reissue and New Colors [ ], row 15); Hot Bird (Reissue and New Colors [ ], row 16)
- **6967**: Dune Daddy (Reissue and New Colors [ ], row 1); Swingin' Wing (Reissue and New Colors [ ], row 2)
- **9206**: Porsche 911 (Reissue and New Colors [ ], row 5); Porsche 911 (Reissue and New Colors [ ], row 6)
- **9241**: Corvette Stingray (Reissue and New Colors [ ], row 8); Corvette Stingray (Reissue and New Colors [ ], row 9)

## Repeated casting-name groups

- **Porsche 911**: Reissue and New Colors [ ], row 5 (Toy # 9206); Reissue and New Colors [ ], row 6 (Toy # 9206)
- **Corvette Stingray**: Reissue and New Colors [ ], row 8 (Toy # 9241); Reissue and New Colors [ ], row 9 (Toy # 9241)
- **Hot Bird**: Reissue and New Colors [ ], row 15 (Toy # 2014); Reissue and New Colors [ ], row 16 (Toy # 2014)

## Interpretation notes

- Different source table schemas are retained without forcing fields into a single source schema. Missing mapped fields remain blank; raw headers and cells are preserved.
- Repeated Toy # values and repeated casting names remain separate source rows. A shared identifier or name does not prove identical physical releases, tooling, or package variants.
- Section headings are source labels, not normalized collection taxonomy.
- 3 blank Toy # values are retained as blank.
- Photo cells empty: 49 of 49.

## Table schemas

- Table 1 (New Castings [ ]): Car Name | Series | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo
- Table 2 (Reissue and New Colors [ ]): Car Name | Series | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo
- Table 3 (Hot Wheels by Year [ ]): Yearly Lists of Basic Line and Other collections
