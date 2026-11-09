# Mainline 1983: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1983/List of 1983 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `53e0c4a826c805925025e0c80c76bea7aa48fed5`
- File size from Git tree: 431,078 bytes
- Manifest SHA-256: `6943ddd612d1507193a1731bf3feb4999466ae6a569f00f7b346342b6e2b58c2`
- Fandom revision: 751644

Machine-readable export: [MAINLINE-1983.csv](MAINLINE-1983.csv). The export preserves source table index, section heading, row position, original headers and every source cell. Blank Toy # values are retained.

## Extraction method

Extracted all five product tables and 67 source rows in source order. The navigation/footer table was excluded.

## QA results

| Check | Result |
|---|---:|
| Product tables | 5 |
| Source rows | 67 |
| Unique nonblank Toy # | 51 |
| Blank Toy # | 7 |
| Repeated Toy # groups | 6 |
| Repeated casting-name groups | 9 |
| Collector # column | Not present |
| Series # column | Not present |
| Photo cells empty | 67 / 67 |

## Table inventory

- Table 1: New Castings [ ]: 15 rows; 12 source columns
- Table 2: Real Riders [ ]: 17 rows; 12 source columns
- Table 3: Reissues [ ]: 26 rows; 12 source columns
- Table 4: Extras Series [ ]: 8 rows; 11 source columns
- Table 5: HiRakers [ ]: 1 rows; 12 source columns

## Repeated Toy # values

- **3919**: '40's Ford 2-Door (New Castings [ ], row 1); '40's Ford 2-Door (Real Riders [ ], row 1); '40's Ford 2-Door (Real Riders [ ], row 2)
- **3923**: Classic Cobra (New Castings [ ], row 6); Classic Cobra (Real Riders [ ], row 5); Classic Cobra (Real Riders [ ], row 6)
- **3915**: Formula Fever (New Castings [ ], row 9); Formula Fever (Real Riders [ ], row 7); Formula Fever (Real Riders [ ], row 8)
- **3917**: Pontiac J-2000 (New Castings [ ], row 12); Rig Wrecker (New Castings [ ], row 13)
- **4370**: Jeep Scrambler (Real Riders [ ], row 9); Jeep Scrambler (Real Riders [ ], row 10)
- **3259**: Jeep CJ-7 (Real Riders [ ], row 13); Jeep CJ-7 (Reissues [ ], row 10)

## Repeated casting-name groups

- **'40's Ford 2-Door**: '40's Ford 2-Door (New Castings [ ], row 1); '40's Ford 2-Door (Real Riders [ ], row 1); '40's Ford 2-Door (Real Riders [ ], row 2)
- **Classic Cobra**: Classic Cobra (New Castings [ ], row 6); Classic Cobra (Real Riders [ ], row 5); Classic Cobra (Real Riders [ ], row 6)
- **Formula Fever**: Formula Fever (New Castings [ ], row 9); Formula Fever (Real Riders [ ], row 7); Formula Fever (Real Riders [ ], row 8)
- **Turbo Streak**: Turbo Streak (New Castings [ ], row 15); Turbo Streak (Real Riders [ ], row 11); Turbo Streak (Real Riders [ ], row 12)
- **Cadillac Seville**: Cadillac Seville (Real Riders [ ], row 4); Cadillac Seville (Reissues [ ], row 4)
- **Jeep Scrambler**: Jeep Scrambler (Real Riders [ ], row 9); Jeep Scrambler (Real Riders [ ], row 10)
- **Jeep CJ-7**: Jeep CJ-7 (Real Riders [ ], row 13); Jeep CJ-7 (Reissues [ ], row 10)
- **Airport Rescue**: Airport Rescue (Reissues [ ], row 11); Airport Rescue (Reissues [ ], row 12)
- **'31 Doozie**: '31 Doozie (Extras Series [ ], row 1); '31 Doozie (Extras Series [ ], row 2)

## Interpretation notes

- New Castings, Real Riders, Reissues and HiRakers use 12 source columns. Extras Series uses 11 and has no Series field.
- The source has a **Series** column in most tables, but no **Series #** or **Collector #** column. Do not infer either identifier from row order or Series labels.
- Seven rows have blank Toy # values; these blanks are retained as source data.
- All 67 Photo cells are empty in the archived HTML tables.
- Repeated Toy # values and repeated casting names are preserved as separate source rows. A shared identifier or name does not prove identical physical releases, tooling, or package variants.
- Table section names are source headings, not normalized collection taxonomy.
- The source's spelling and wording, including the Extras Series header `Removeable parts/notes`, are retained in Raw source headers/cells.

## Table schemas

- Table 1 (New Castings [ ]): Casting Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 2 (Real Riders [ ]): Casting Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 3 (Reissues [ ]): Casting Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 4 (Extras Series [ ]): Casting Name | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Removeable parts/notes | Photo
- Table 5 (HiRakers [ ]): Casting Name | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
