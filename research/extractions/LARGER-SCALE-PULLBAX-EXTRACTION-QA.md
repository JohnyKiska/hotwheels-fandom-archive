# Pullbax extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Larger Scale/Pullbax _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `ac0f4895130987a7c3182e5f67b7494bd043b27e`
- Manifest file size: 358997 bytes
- Manifest SHA-256: `6F7A01EFB223B7A87C4AB2BED72E04B6103CD611C48F0E2C74F2C18DEDF140E8`
- Fandom revision ID: 787309
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 5
- Product rows: 23
- Export columns: 21
- Other HTML tables excluded: 0

## Product tables
- 2004: 7 rows, 7 source columns. Headers: Toy # | Name | Year | Country | Notes | Photo | Photo
- 2006: 4 rows, 6 source columns. Headers: Toy # | Name | Year | Country | Notes | Photo
- 2008: 3 rows, 6 source columns. Headers: Toy # | Name | Year | Country | Notes | Photo
- Speed Racer: 5 rows, 6 source columns. Headers: Toy # | Name | Year | Country | Notes | Photo
- 2009: 4 rows, 6 source columns. Headers: Toy # | Name | Year | Country | Notes | Photo

## QA notes
- Product tables identified by toy-number and casting/model/name headers; navigation and collapsible gallery tables excluded.
- Source table and row order retained.
- Raw source headers and cell text/image filenames preserved in the final two columns.
- Matching toy numbers, collection numbers, year, series labels, body colors, wheel types, country and notes mapped where source headers support them; remaining fields are retained in raw source data.
- Gallery extraction deferred.

## Output
- `research/extractions/LARGER-SCALE-PULLBAX.csv`
