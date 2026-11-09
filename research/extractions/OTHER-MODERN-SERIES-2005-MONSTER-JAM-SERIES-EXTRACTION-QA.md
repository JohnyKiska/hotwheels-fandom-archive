# 2005 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2005 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `8a4759b5b4df5d2e52fbf9faa7a36b17f93817fc`
- Manifest file size: 380,053 bytes
- Manifest SHA-256: `76E0D2B4900C5C8E96EE6F5A2B4CA96B538E742AD778FC876AEFC9F704B232C8`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 2
- Product rows: 62
- Export columns: 21
- Excluded tables: 1 (navigation/collapsible tables or non-product structures)

## Product tables
- Monster Trucks [ ]: 54 rows, 5 source columns. Headers: Toy # | Series # | Truck | Subset | Photo
- Multipacks [ ]: 8 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo

## QA notes
- Source table order and row order are retained.
- Raw source headers and cells are preserved in the final two columns.
- Fields not mapped to the normalized schema remain preserved in raw source data.
- Bundle contents and notes are retained as source notes, not expanded into inferred individual releases.
- Gallery extraction is deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2005-MONSTER-JAM-SERIES.csv`
