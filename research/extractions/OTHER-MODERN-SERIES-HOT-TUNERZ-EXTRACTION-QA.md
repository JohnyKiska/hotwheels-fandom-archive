# Hot Tunerz extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Tunerz _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `86d03069324d69c9bf137679d51c43f581dbed37`
- Manifest file size: 398,149 bytes
- Manifest SHA-256: `803D3F34D2741BE8AE514161970B14D469EA0FF07337DB1826716624E2122A4B`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 4
- Product rows: 68
- Export columns: 21
- Excluded tables: 0 (non-product/navigation or single-column tables)

## Product tables
- 1:55 Scale Models [ ]: 56 data rows, 9 source columns. Headers: Casting Name | Body Color | Tampos | Sponsor | Wheel Type | Toy # | Country | Notes | Photo
- 1:20 Scale Models [ ]: 6 data rows, 9 source columns. Headers: Casting Name | Body Color | Tampos | Sponsor | Wheel Type | Toy # | Country | Notes | Photo
- Rally Hot Tunerz [ ]: 3 data rows, 6 source columns. Headers: Casting Name | Body Color | Tampos | Wheel Type | Notes | Photo
- Rally Group X [ ]: 3 data rows, 6 source columns. Headers: Casting Name | Body Color | Tampos | Wheel Type | Notes | Photo

## QA notes
- Product-table rows are retained in source order.
- Original source headers and cell content are preserved in the final two columns.
- Unmapped source columns remain available in Raw source headers and Raw source cells.
- Empty values remain empty; no casting identity or release equivalence has been inferred.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-HOT-TUNERZ.csv`
