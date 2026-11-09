# 2011 Monster Jam Series extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Other Modern Series/Hot Wheels Monster Jam/2011 Monster Jam Series _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `3f7d2664350e8a65a919bd72f970732feda331ad`
- Manifest file size: 456,743 bytes
- Manifest SHA-256: `0D4B875ED2C9384F1AD833C546C3656AE6E60F42C9B33D4BCC294CB597FF1C79`
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 8
- Product rows: 125
- Export columns: 21
- Excluded tables: 1 (navigation/collapsible)

## Product tables
- Trucks [ ]: 81 rows, 4 source columns. Headers: # | Truck Name | Subset | Photo
- Target Holiday Edition Trucks [ ]: 6 rows, 4 source columns. Headers: # | Truck Name | Subset | Photo
- Walmart Holiday Edition Trucks [ ]: 8 rows, 4 source columns. Headers: # | Truck Name | Subset | Photo
- Deluxe Jumpers [ ]: 6 rows, 3 source columns. Headers: Truck Name | Subset | Photo
- Flip Crashers [ ]: 8 rows, 3 source columns. Headers: Truck Name | Subset | Photo
- Heavy Duty Haulers [ ]: 4 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo
- Multipacks [ ]: 7 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo
- Playset [ ]: 5 rows, 5 source columns. Headers: Toy # | Name | Contents | Notes | Photo

## QA notes
- Source table and row order retained.
- Raw source headers and cells preserved in the final two columns.
- Source values are retained without inferred release equivalence.
- Gallery extraction deferred.

## Output
- `research/extractions/OTHER-MODERN-SERIES-2011-MONSTER-JAM-SERIES.csv`
