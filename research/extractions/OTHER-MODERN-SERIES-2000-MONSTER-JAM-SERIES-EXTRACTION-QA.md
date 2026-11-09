# 2000 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2000 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `a7b4b9eca155e1a96b4054f92dfa6b878f971ce1`
- Manifest file size: 331,441 bytes
- Manifest SHA-256: `57952EBAB44708ED4B644C486C5A244ED0660D79DB04EEABB6EFBAE9F5F6AA86`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 4
- Export columns: 21
- Excluded tables: 1 (non-product/navigation or single-column tables)

## Product tables
- Monster Trucks [ ]: 4 data rows, 5 source columns. Headers: Toy # | Truck | Subset | Photo 1 (Short Card) | Photo 2 (Long Card)

## QA notes
- Product-table rows are retained in source order.
- Original source headers and cell content are preserved in the final two columns.
- Unmapped source columns remain available in Raw source headers and Raw source cells.
- Empty values remain empty; no casting identity or release equivalence has been inferred.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2000-MONSTER-JAM-SERIES.csv`
