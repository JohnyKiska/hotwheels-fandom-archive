# 2008 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2008 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `d6d4a2cf1571365e9330921de3829bb5500d434d`
- Manifest file size: 391,568 bytes
- Manifest SHA-256: `E652D86492E182D1734E4AF0FA4EE92D224A7B92950DF3515ADF32ABFE813340`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 4
- Product rows: 83
- Export columns: 21
- Excluded tables: 1 (navigation/collapsible)

## Product tables
- Trucks [ ]: 70 rows, 4 source columns. Headers: # | Truck Name | Subset | Photo
- Heavy Duty Haulers [ ]: 4 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo
- Multipacks [ ]: 7 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo
- Playset [ ]: 2 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo

## QA notes
- Source table and row order retained.
- Raw source headers and cells preserved in the final two columns.
- Casting labels, truck names, subsets and package contents remain source values; no inferred release equivalence.
- Gallery extraction deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2008-MONSTER-JAM-SERIES.csv`
