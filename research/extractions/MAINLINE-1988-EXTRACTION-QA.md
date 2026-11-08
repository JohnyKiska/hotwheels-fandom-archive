# Mainline 1988: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1988/List of 1988 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `f9d64266cd391b7412c75ff2faead68db862e1d1`
- File size: 373,400 bytes (Git tree size)
- Manifest SHA-256: `f18142793af6633d38aa12be266930d144de9d1aba7ef926f24a480a50b1d28e`
- Fandom revision: 765062

Machine-readable export: [MAINLINE-1988.csv](MAINLINE-1988.csv). It preserves both tables, all 11 source columns, row order and source section.

## Extraction method

Extracted two product tables and 27 rows. Both tables use the same 11-column schema. There is no Collector # field on the 1988 page.

## QA results

| Check | Result |
|---|---:|
| Product tables | 2 |
| Source rows | 27 |
| New Castings | 13 |
| Reissues | 14 |
| Distinct nonblank Toy # | 25 |
| Blank Toy # rows | 0 |
| Repeated Toy # groups | 2 |
| Rows with Notes | 3 |

Repeated Toy # groups:
- Toy #4741: 2 rows
- Toy #5026: 2 rows

## Interpretation notes

- Toy #5026 appears for Alien in two colors (Blue & Silver; Red & Silver). The Blue & Silver row is marked `Short run color`; preserve both variants.
- Toy #4741 appears for Talbot Lago in two colors (Burgundy; White). The Burgundy row is marked `Short run color`; preserve both variants.
- The page contains no Collector # field. Do not backfill one from later years.
- Source Series labels include Workhorses, Speed Fleet, Speed Demons, 1988 Hot Wheels, Action Command and Classics. Keep the literal Series value.
- Fandom is a secondary source; the note `Short run color` is a source assertion and should remain attributed to the page.
