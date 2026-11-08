# Mainline 1994: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1994/List of 1994 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `30896d156d7a1d8ba6071cae6796e75ef7f87c08`
- File size: 361,452 bytes (Git tree size)
- Manifest SHA-256: `b82dfa984c29b281d168ba387a0e57280bd67500e695953d3121ad9b8e21f36b`
- Fandom revision: 783555

Machine-readable export: [MAINLINE-1994.csv](MAINLINE-1994.csv). All 12 source columns are preserved, including Color, Tampo, Base Color / Type, Window Color, Interior Color, Wheel Type, Notes and Photo.

## Extraction method

Extracted both product tables and all 14 source rows. The 1994 page uses a substantially richer 12-column schema rather than the 1995/1996 Toy # / Collector # / Model Name layout. No column remapping based on the later schema was applied.

## QA results

| Check | Result |
|---|---:|
| Product tables | 2 |
| Source rows | 14 |
| New Models rows | 5 |
| Reissues rows | 9 |
| Unique Col # values | 13 |
| Distinct nonblank Toy # values | 12 |
| Rows with blank Toy # | 1 |
| International row | 1 |
| BMW 850i rows | 2 |

## Special cases requiring preservation

- **BMW 850i, Col #255, Toy #5667:** two rows differ by Wheel Type (UH vs GUH). Preserve as separate source variants; do not deduplicate.
- **Sol-Aire CX-4, Col #254:** Toy # is blank in source. Keep the blank and flag for external validation.
- **Road Roller:** Col # is the literal text `INTL`; Series is `1994 INTL`. Do not coerce the identifier to numeric.
- **Tough Customer, Col #159:** source row appears misaligned/suspicious: `Interior Color` is `13192`, `Wheel Type` is `Black MGW`, and `Toy #` is `13192`. Preserve raw columns and flag the row rather than silently correcting it.

## Table inventory

- Table 1, New Models: 5 rows.
- Table 2, Reissues: 9 rows.

## Interpretation notes

- The 1994 page's fields describe release/variant details; Color, Tampo, base/window/interior colors and Wheel Type are not interchangeable attributes.
- Collector number and Toy # are distinct identifiers.
- Fandom is a secondary source; confirm missing or suspicious fields with packaging, catalogues or other primary evidence before normalization.
