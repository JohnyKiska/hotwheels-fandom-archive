# Hot Import Nights extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Import Nights _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `89bd96f13edb1f3e7c1bd27986f2ecf681d641e8`
- Manifest file size: 373,518 bytes
- Manifest SHA-256: `D0C5D0F0C57EE1B6EE6155795293AE159FA053C58E17A25635D7407B84BE7C2E`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 2
- Product rows: 32
- Export columns: 21
- Excluded tables: 0 (non-product/navigation or single-column tables)

## Product tables
- Hot Import Nights [ ]: 16 data rows, 10 source columns. Headers: Toy # | Casting | Color | Tampo | Base Color / / / Type | Wheel Type | Country | Notes | Photo Packaged | Photo Loose
- HIN D-Force [ ]: 16 data rows, 10 source columns. Headers: Toy # | Casting | Color | Tampo | Base Color / / / Type | Wheel Type | Country | Notes | Photo Packaged | Photo Loose

## QA notes
- Product-table rows are retained in source order.
- Original source headers and cell content are preserved in the final two columns.
- Unmapped source columns remain available in Raw source headers and Raw source cells.
- Empty values remain empty; no casting identity or release equivalence has been inferred.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-HOT-IMPORT-NIGHTS.csv`
