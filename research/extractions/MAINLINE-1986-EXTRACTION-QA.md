# Mainline 1986: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1986/List of 1986 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `d073bd5d8ce236c8e0947cdee36cdebe77eda140`
- File size: 376,838 bytes (Git tree size)
- Manifest SHA-256: `911abf23597e1efccf757aca81c1fafb2d2fd029e084f48b9bc1ca2b67db8ee1`
- Fandom revision: 755450

Machine-readable export: [MAINLINE-1986.csv](MAINLINE-1986.csv). All three source tables, their 12-/11-column schemas, row order and source fields are preserved.

## Extraction method

Extracted three tables and 26 rows: New Castings, Reissues and Real Riders.

## QA results

| Check | Result |
|---|---:|
| Product tables | 3 |
| Source rows | 26 |
| New Castings | 8 |
| Reissues | 13 |
| Real Riders | 5 |
| Distinct nonblank Toy # | 20 |
| Repeated Toy # groups | 6 |
| Country values | Malaysia: 21; Hong Kong: 5 |
| Blank Toy # rows | 0 |

Repeated Toy # groups:
- Toy #2057: 2 rows
- Toy #2058: 2 rows
- Toy #2520: 2 rows
- Toy #2534: 2 rows
- Toy #2537: 2 rows
- Toy #2539: 2 rows

## Specific cases

- Toy #2058 Cargoyle: Malaysia (Orange) and Hong Kong (Yellow, marked `Only in set`).
- Toy #2057 Double Demon: two Hong Kong color entries (Red and Light Green); Light Green is marked `Only in set`.
- Toy #2520 Race Ace appears twice in Reissues with minor Tampo wording differences.
- Toy #2537 Rescue Ranger appears in Reissues and Real Riders, with different Wheel Type (BW vs RR White).
- Toy #2539 Jeep CJ-7 appears in Reissues and Real Riders, with different Wheel Type notation.
- Toy #2534 is used for two different Real Riders entries: Path Beater and Power Plower. Treat as a source-level identifier collision pending validation.

## Interpretation notes

- Country is an explicit source field for New Castings/Reissues and is absent from the Real Riders table. Preserve Malaysia/Hong Kong as release metadata, not as casting identity.
- "Only in set" and original-name notes are source assertions; do not convert them into proven exclusivity or casting relationships without corroboration.
- No Collector # field is present in these 1986 tables.
- Fandom is a secondary source; verify Toy #2534 collision and repeated entries against packaging/catalogues.
