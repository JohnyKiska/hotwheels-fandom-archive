# 2009 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2009 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `f6d58b645fc4b18c4c8065bcc6d82fc9496c1144`
- Manifest file size: 409,400 bytes
- Manifest SHA-256: `AB3D3D001AAFE10D37B814868FC84229FB948089C5D522A8AB324FFA5DE931A0`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 5
- Product rows: 105
- Export columns: 21
- Excluded tables: 1 (navigation/collapsible)

## Product tables
- Trucks [ ]: 79 rows, 4 source columns. Headers: # | Truck Name | Subset | Photo
- Easter Beast Trucks [ ]: 10 rows, 4 source columns. Headers: # | Truck Name | Subset | Photo
- Heavy Duty Haulers [ ]: 4 rows, 4 source columns. Headers: # | Casting Name | Truck Name | Photo
- Multipacks [ ]: 8 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo
- Playset [ ]: 4 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo

## QA notes
- Source table and row order retained.
- Raw source headers and cells preserved in the final two columns.
- Casting labels, truck names, subsets and package contents remain source values; no inferred release equivalence.
- Gallery extraction deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2009-MONSTER-JAM-SERIES.csv`
