# Premium 1:43 extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Larger Scale/Premium 1_43 _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `087267a3c416ee6ce6a340dddafe231dda772a24`
- Manifest file size: 425636 bytes
- Manifest SHA-256: `CE84F5A2E3BCB477C3B3121B1D5D053F42BDEBA90D17E927DFAFA292B62FE28C`
- Fandom revision ID: 795588
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 5
- Product rows: 41
- Export columns: 21
- Other HTML tables excluded: 1

## Product tables
- 2023: 6 rows, 7 source columns. Headers: Toy # | Series # | Casting Name | Body Color | Notes | Photo Loose | Photo Carded
- 2024: 11 rows, 7 source columns. Headers: Toy # | Series # | Casting Name | Body Color | Notes | Photo Loose | Photo Carded
- 2025: 12 rows, 7 source columns. Headers: Toy # | Series # | Casting Name | Body Color | Notes | Photo Loose | Photo Carded
- 2026: 4 rows, 7 source columns. Headers: Toy # | Series # | Casting Name | Body Color | Notes | Photo Loose | Photo Carded
- 2026: 8 rows, 8 source columns. Headers: Toy # | Pack name | Casting | Body Color | Wheel Type | Notes | Photo Loose | Photo Carded

## QA notes
- Product tables identified by toy-number and casting/model/name headers; navigation and collapsible gallery tables excluded.
- Source table and row order retained.
- Raw source headers and cell text/image filenames preserved in the final two columns.
- Matching toy numbers, collection numbers, year, series labels, body colors, wheel types, country and notes mapped where source headers support them; remaining fields are retained in raw source data.
- Gallery extraction deferred.

## Output
- `research/extractions/LARGER-SCALE-PREMIUM-1-43.csv`
