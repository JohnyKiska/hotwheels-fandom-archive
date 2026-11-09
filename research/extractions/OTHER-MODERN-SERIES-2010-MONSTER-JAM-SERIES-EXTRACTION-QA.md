# 2010 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2010 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `5e18b630050843a919c98df7e08d7e1b14c1ec03`
- Manifest file size: 521,565 bytes
- Manifest SHA-256: `A8BA4393623D976F9711D0D017D81FEA0D30C9C87B8E80304807F4D50AF2F719`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 5
- Product rows: 97
- Export columns: 21
- Excluded tables: 1 (navigation/collapsible)

## Product tables
- Trucks [ ]: 77 rows, 4 source columns. Headers: # | Truck Name | Subset | Photo
- Easter Beast Trucks [ ]: 8 rows, 4 source columns. Headers: # | Truck Name | Subset | Photo
- Deluxe Jumpers [ ]: 8 rows, 3 source columns. Headers: Truck Name | Subset | Photo
- Multipacks [ ]: 2 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo
- Playset [ ]: 2 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo

## QA notes
- Source table and row order retained.
- Raw source headers and cells preserved in the final two columns.
- Casting labels, truck names, subsets and package contents remain source values; no inferred release equivalence.
- Gallery extraction deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2010-MONSTER-JAM-SERIES.csv`
