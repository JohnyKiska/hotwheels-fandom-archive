# Mainline 1987: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1987/List of 1987 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `8b8c34034c31cb4cc5f0f278b6c07d00cd69dba5`
- File size: 373,508 bytes (Git tree size)
- Manifest SHA-256: `7e984bfdd92f56b4fc82e35d47f90d98b0ea6b331b8b9ca4fbf08bc882e179bd`
- Fandom revision: 754002

Machine-readable export: [MAINLINE-1987.csv](MAINLINE-1987.csv). All three product tables are retained, including the four-column Real Riders table.

## Extraction method

Extracted 3 product tables and 23 rows: New Castings, Reissues and Real Riders. The first two use 11 columns; Real Riders uses four.

## QA results

| Check | Result |
|---|---:|
| Product tables | 3 |
| Source rows | 23 |
| New Castings | 12 |
| Reissues | 10 |
| Real Riders | 1 |
| Distinct nonblank Toy # | 20 |
| Blank Toy # rows | 0 |
| Repeated Toy # groups | 2 |
| Collector # field present | No |

Repeated Toy # groups:
- Toy #1897: three Ferrari Testarossa entries (black, white, and a red Turbo Trax Turbo Glo Set-only entry).
- Toy #7527: two Pontiac Fiero 2M4 entries differing by Wheel Type (GHO vs UH).

## Interpretation notes

- No Collector # field exists in these tables. Do not backfill one.
- Real Riders is a separate source section with its own four-column schema; it is not a row in the 11-column New Castings/Reissues schema.
- Preserve Series labels and Notes literally.
- Fandom is a secondary source and does not independently establish casting/tooling identity.
