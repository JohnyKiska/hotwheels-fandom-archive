# Mainline 2010 (International list): extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2010/List of 2010 Hot Wheels (International) _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `2ef979cd1dda8236096ed4eb9c490aff5b6ce8e1`
- File size: 593,595 bytes
- Manifest SHA-256: `005479a8abb31b038071b1699146e27806416e4319d75b81109db68ed0d91644`
- Fandom revision: 815650

Machine-readable export: [MAINLINE-2010-INTERNATIONAL.csv](MAINLINE-2010-INTERNATIONAL.csv). It preserves table index, section heading, row order, all six source columns and raw text.

## QA results

| Check | Result |
|---|---:|
| Product tables | 24 |
| Source rows | 228 |
| Unique Toy # | 226 |
| Unique Collector # | 214 |
| Collector # range | 001–214, no gaps |
| Rows marked `(2nd Color)` | 1 |
| Treasure Hunt rows | 12 |
| Super Treasure Hunt rows | 12 |
| Missing required source fields | 0 |
| Photo cells empty | 228 / 228 |

Collector # duplication is meaningful in this source:

- Collector #053–064 each appears twice: once as Treasure Hunt and once as Super Treasure Hunt, with different Toy #.
- Collector #087 appears three times for AMC Javelin AMX color entries, all with Toy #R7504.
- Preserve these row-level variants; do not assume Collector # uniquely identifies one physical release in the International source.

## Interpretation notes

- The International page is not a duplicate copy of the ordinary 2010 list. It has a distinct table structure and 228 rows.
- Preserve its own Collector # scope, table headings and source row order.
- Toy # overlap with the ordinary list is a candidate cross-listing relationship, not proof that the exact release/packaging is identical.
