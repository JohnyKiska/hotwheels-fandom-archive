# Hot Wheels 1:87 Scale Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels 1_87 Scale Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `1d4274b87fc32af75aae788b65f8d985e813d69e`
- Manifest file size: 424,346 bytes
- Manifest SHA-256: `AC3D63F481E6DE68A68B983B16543A62AAF862D5620FC9B4E5BDE086786AA165`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 4
- Product rows: 59
- Export columns: 21
- Excluded tables: 0 (non-product/navigation or single-column tables)

## Product tables
- 2007 [ ]: 18 data rows, 8 source columns. Headers: Model Name | Color | Tampos | Wheel Type | Toy # | Country | Notes | Photo
- 2008 [ ]: 11 data rows, 8 source columns. Headers: Model Name | Color | Tampos | Wheel Type | Toy # | Country | Notes | Photo
- Speed Racer [ ]: 5 data rows, 8 source columns. Headers: Model Name | Color | Tampos | Wheel Type | Toy # | Country | Notes | Photo
- 2009 [ ]: 25 data rows, 8 source columns. Headers: Model Name | Color | Tampos | Wheel Type | Toy # | Country | Notes | Photo

## QA notes
- Product-table rows are retained in source order.
- Original source headers and cell content are preserved in the final two columns.
- Unmapped source columns remain available in Raw source headers and Raw source cells.
- Empty values remain empty; no casting identity or release equivalence has been inferred.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-HOT-WHEELS-1-87-SCALE-SERIES.csv`
