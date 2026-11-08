# Mainline 1993: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1993/List of 1993 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `5c87ed8545c8a6441046cc45e208037523f6885b`
- File size: 425,103 bytes (Git tree size)
- Manifest SHA-256: `ce0b018217e08dc56353565b4187b4cd38c3cc147b72249bc629ef8cc83ce012`
- Fandom revision: 797943

Machine-readable export: [MAINLINE-1993.csv](MAINLINE-1993.csv). It preserves all source columns and table boundaries. The CSV maps source fields by header name and keeps raw header/cell sequences to avoid losing differences among the five table schemas.

## Extraction method

Extracted all five product tables and 72 source rows. The page mixes annual list records, sub-series entries, and themed series tables. Their identifiers are not interchangeable.

## QA results

| Check | Result |
|---|---:|
| Product tables | 5 |
| Source rows | 72 |
| New Castings | 10 |
| Reissues | 32 |
| Tattoo Machines | 13 |
| Demolition Man | 9 |
| 25th Anniversary Series | 8 |
| Distinct nonblank Toy # | 64 |
| Distinct nonblank Col # in New Castings/Reissues | 36 |
| Blank Toy # rows | 4 |
| Blank Col # rows in New Castings/Reissues | 3 |

### Repeated and conflicting identifiers

Collector number repeats:
- Col #149: 2 rows
- Col #197: 2 rows
- Col #224: 2 rows

Toy # repeats:
- Toy #2781: 2 rows
- Toy #3502: 2 rows
- Toy #4314: 2 rows
- Toy #5667: 2 rows

### Specific cases

- BMW 850i, Col #149 / Toy #5667 appears twice in Reissues with different Wheel Type values (HO and LIW).
- Col #197 is used by two different Reissues: Corvette Split Window (Toy #3092) and Gleamer Patrol (Toy #1691). Treat as a source identifier conflict pending validation.
- Zombot, Col #224 appears twice with different Toy # values (3852 and 4346) and different color descriptions.
- Auburn 852, Toy #4314 appears twice in Reissues; the second row has blank Col # and a different color description.
- Path Beater and Bywayman share Toy #2781 in Reissues.
- Rapid Transit appears twice in Tattoo Machines with Toy #3502, different colors, and the same Series Rename (Bus Boys).
- Four Tattoo Machines rows have blank Toy #: BMW M1, Science Friction, Speed Blaster and Road Pirate.
- Demolition Man has a distinct `# in Series` identifier (1/9–9/9), not an annual Collector #.
- Tattoo Machines has a `Series Rename` column; preserve original Car name and Series Rename separately.

## Table inventory

- Table 1, New Castings [ ]: 10 rows; 11 columns (Col # | Car name | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo)
- Table 2, Reissues [ ]: 32 rows; 11 columns (Col # | Car name | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Notes | Photo)
- Table 3, Tattoo Machines [ ]: 13 rows; 10 columns (Car name | Color | Tampo | Base Color / Type | Window Color | Interior Color | Wheel Type | Toy # | Series Rename | Photo)
- Table 4, Demolition Man [ ]: 9 rows; 5 columns (Toy # | # in Series | Series Name | Casting | Photo)
- Table 5, 25th Anniversary Series [ ]: 8 rows; 10 columns (Toy # | Casting Name | Body Color | Base Color | Window Color | Interior Color | Wheel Type | Country | Notes | Photo)

## Interpretation notes

- New Castings/Reissues use `Col #`; Tattoo Machines does not have this field; Demolition Man uses `# in Series`; 25th Anniversary Series has Toy # and Casting Name but no Collector #. Keep these identifier scopes separate.
- Repeated numbers may represent wheel variants, conflicting source numbering, alternate colorways, or source errors. Do not deduplicate or infer identity from a number alone.
- Four blank Toy # cells in Tattoo Machines are source omissions, not zeroes.
- Fandom is a secondary source; verify conflicting identifiers and missing values against packaging/catalogues before normalization.
