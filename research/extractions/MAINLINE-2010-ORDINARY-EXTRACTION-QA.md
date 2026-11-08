# Mainline 2010 (ordinary list): extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2010/List of 2010 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `26c08a2134f9c4df6b4c634a2cf9b3c4e941966c`
- File size: 808,271 bytes
- Manifest SHA-256: `08de99b8152225a6c44eabec762fa2d82e094e6b559a1befbf4b34037ea362d7`
- Fandom revision: 815649

Machine-readable export: [MAINLINE-2010-ORDINARY.csv](MAINLINE-2010-ORDINARY.csv). It preserves table index, section heading, row order, all six source columns and raw text.

## QA results

| Scope | Tables | Rows |
|---|---:|---:|
| Annual Mainline tables | 26 | 422 |
| Goodyear Tire Exclusives | 1 | 8 |
| BF Goodrich Tire Exclusives | 1 | 10 |
| Total source rows | 28 | 440 |

Annual Mainline checks:

- 252 unique Toy # values.
- 240 unique Collector # values, continuous 001–240.
- 125 rows marked `(2nd Color)`.
- 12 Treasure Hunt and 12 Super Treasure Hunt rows.
- No missing Toy #, Collector #, Model Name, Series or Series # values.
- All Photo cells are empty.

The 18 tire-exclusive rows all use Toy # values already present in the annual Mainline tables. Sixteen rows are exact six-column repeats. Two BF Goodrich rows differ from their Mainline counterpart:

- R7531, Collector #106: `'41 Willys (2nd Color)`.
- R7638, Collector #209: `Phantom Racer`.

Preserve both exclusive-section appearances and their exact source values; do not create new unique Toy # records from the repeated listing alone.

## Interpretation notes

- Toy # is not a unique row key in 2010 because multiple color variants share a Toy #.
- Collector # is unique within the annual list and continuous 001–240.
- Keep tire-exclusive section provenance even when rows repeat Mainline content.
- This ordinary list is a separate source dataset from the 2010 International list.
