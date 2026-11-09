# Mainline 1981: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1981/List of 1981 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `9650fc85ba0c1c4b45295d4c0b44aadd5df01c88`
- File size from Git tree: 385,682 bytes
- Manifest SHA-256: `525efb8555d39c21bb1f9fb40f7e085df1ced4ee301d38c2cfce8b032f5e70e3`
- Fandom revision: 765056

Machine-readable export: [MAINLINE-1981.csv](MAINLINE-1981.csv). The export preserves source table index, section heading, row position, original headers and every source cell. Blank Toy # values are retained.

## Extraction method

Extracted all four product tables and 27 source rows in source order. The navigation/footer table was excluded.

## QA results

| Check | Result |
|---|---:|
| Product tables | 4 |
| Source rows | 27 |
| Unique nonblank Toy # | 25 |
| Blank Toy # | 1 |
| Repeated Toy # groups | 1 |
| Repeated casting-name groups | 1 |
| Collector # column | Not present |
| Series # column | Not present |
| Photo cells empty | 27 / 27 |

## Table inventory

- Table 1: New Castings [ ]: 12 rows; 11 source columns
- Table 2: Repaints [ ]: 10 rows; 10 source columns
- Table 3: Scene Machines [ ]: 3 rows; 10 source columns
- Table 4: Heroes [ ]: 2 rows; 10 source columns

## Repeated Toy # values

- **9649**: '31 Doozie (Repaints [ ], row 2); '31 Doozie (Repaints [ ], row 3)

## Repeated casting-name groups

- **'31 Doozie**: Repaints [ ], row 2 (Toy # 9649); Repaints [ ], row 3 (Toy # 9649)

## Interpretation notes

- The source tables use different schemas. New Castings includes Series; Repaints and Scene Machines include Notes; Heroes uses Original Casting, Year and Series Rename rather than the standard Car Name/Series fields.
- The Heroes table identifies Iron Man and Spider Man as original castings, gives 1981 as Year, and lists Series Rename values Iron Man and Silver Surfer respectively. The Spider Man row's tampo text says “Silver Surfer”. These source labels are preserved as assertions, not normalized identities.
- Repaints contains two separate '31 Doozie rows with the same Toy # 9649 but different colors/fender descriptions. They remain separate source rows.
- The source has no Collector # or Series # columns. Do not infer either identifier from row order or section headings.
- 1 rows have blank Toy # values; blanks are retained.
- All 27 Photo cells are empty in the archived HTML tables.
- Repeated Toy # values and repeated casting names are preserved as separate source rows. A shared identifier or name does not prove identical physical releases, tooling, or package variants.
- Section names are source headings, not normalized collection taxonomy.
 
## Table schemas

- Table 1 (New Castings [ ]): Car Name | Series | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo
- Table 2 (Repaints [ ]): Car Name | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo
- Table 3 (Scene Machines [ ]): Car Name | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo
- Table 4 (Heroes [ ]): Original Casting | Year | Color | Tampo | Base Color / Type | Window Color | Interior Color | Toy # | Series Rename | Photo
