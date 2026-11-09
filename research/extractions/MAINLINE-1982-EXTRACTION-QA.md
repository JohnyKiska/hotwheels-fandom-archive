# Mainline 1982: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1982/List of 1982 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `d9ef1c1de8e999a17ec646cce30cbf1cd99fcfae`
- File size from Git tree: 455,810 bytes
- Manifest SHA-256: `80e5c7086f85f4ee1ea458270fafcdf93f42e0bf7738340437c731c95112ef1b`
- Fandom revision: 751644

Machine-readable export: [MAINLINE-1982.csv](MAINLINE-1982.csv). The export preserves source table index, section heading, row position, original headers and every source cell. Blank Toy # values are retained.

## Extraction method

Extracted all five product tables and 90 source rows in source order. The navigation/footer table was excluded.

## QA results

| Check | Result |
|---|---:|
| Product tables | 5 |
| Source rows | 90 |
| Unique nonblank Toy # | 74 |
| Blank Toy # | 9 |
| Repeated Toy # groups | 6 |
| Repeated casting-name groups | 9 |
| Collector # column | Not present |
| Series # column | Not present |
| Photo cells empty | 90 / 90 |

## Table inventory

- Table 1: New Castings [ ]: 25 rows; 11 source columns
- Table 2: Reissues [ ]: 48 rows; 11 source columns
- Table 3: Megaforce Series [ ]: 6 rows; 11 source columns
- Table 4: HiRakers [ ]: 5 rows; 13 source columns
- Table 5: Workhorses [ ]: 6 rows; 13 source columns

## Repeated Toy # values

- **5182**: Camaro Z-28 (New Castings [ ], row 5); Camaro Z-28 (New Castings [ ], row 6)
- **3254**: Construction Crane (New Castings [ ], row 7); Construction Crane (New Castings [ ], row 8)
- **9037**: Malibu Grand Prix (New Castings [ ], row 15); Malibu Grand Prix (Reissues [ ], row 3)
- **1693**: Chevy Citation (Reissues [ ], row 14); Chevy Citation (Reissues [ ], row 15)
- **7649**: Super Van (Reissues [ ], row 36); Super Van (Reissues [ ], row 37); Super Van (Reissues [ ], row 39)
- **5270**: Personnel Carrier (Megaforce Series [ ], row 4); Personnel Carrier (Megaforce Series [ ], row 5)

## Repeated casting-name groups

- **Camaro Z-28**: Camaro Z-28 (New Castings [ ], row 5); Camaro Z-28 (New Castings [ ], row 6)
- **Construction Crane**: Construction Crane (New Castings [ ], row 7); Construction Crane (New Castings [ ], row 8)
- **Malibu Grand Prix**: Malibu Grand Prix (New Castings [ ], row 15); Malibu Grand Prix (Reissues [ ], row 3)
- **Turbo Mustang**: Turbo Mustang (Reissues [ ], row 11); Turbo Mustang (Reissues [ ], row 12); Turbo Mustang (Reissues [ ], row 13)
- **Chevy Citation**: Chevy Citation (Reissues [ ], row 14); Chevy Citation (Reissues [ ], row 15)
- **Royal Flash**: Royal Flash (Reissues [ ], row 31); Royal Flash (Reissues [ ], row 32)
- **Super Van**: Super Van (Reissues [ ], row 36); Super Van (Reissues [ ], row 37); Super Van (Reissues [ ], row 39)
- **Omni 024**: Omni 024 (Reissues [ ], row 43); Omni 024 (Reissues [ ], row 44)
- **Personnel Carrier**: Personnel Carrier (Megaforce Series [ ], row 4); Personnel Carrier (Megaforce Series [ ], row 5)

## Interpretation notes

- New Castings, Reissues and Megaforce Series use 11 source columns. HiRakers and Workhorses use 13 columns and include Year and Series fields.
- The source has Series labels in selected tables, but no Collector # or Series # columns. Do not infer either identifier from row order or Series labels.
- Nine rows have blank Toy # values; these blanks are retained.
- All 90 Photo cells are empty in the archived HTML tables.
- Repeated Toy # values and repeated casting names are preserved as separate source rows. A shared identifier or name does not prove identical physical releases, tooling, or package variants.
- Table section names are source headings, not normalized collection taxonomy.
- Source notes such as “originally released as …” remain source assertions and are not independently verified release/tooling relationships.

## Table schemas

- Table 1 (New Castings [ ]): Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Photo
- Table 2 (Reissues [ ]): Name | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 3 (Megaforce Series [ ]): Name | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 4 (HiRakers [ ]): Name | Year | Series | Color | Tampo | Base Color | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 5 (Workhorses [ ]): Name | Year | Series | Color | Tampo | Base Color | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
