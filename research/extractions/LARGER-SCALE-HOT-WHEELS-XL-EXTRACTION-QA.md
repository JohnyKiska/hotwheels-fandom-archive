# Hot Wheels XL extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Larger Scale/Hot Wheels XL _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `c4ee8b17257814dd1950cb6830fd177fc70dfb40`
- Manifest file size: 464511 bytes
- Manifest SHA-256: `84A00C0A2E002E554835052DE475302C8EB4C09AA3491AC0E3DE2FD0492EE866`
- Fandom revision ID: 815549
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 2
- Product rows: 39
- Export columns: 21
- Other HTML tables excluded: 1

## Product tables
- 2026: 24 rows, 6 source columns. Headers: Toy # | Col.# | Mix | Model Name | Photo Open | Photo Carded
- 2027: 15 rows, 6 source columns. Headers: Toy # | Col.# | Mix | Model Name | Photo Open | Photo Carded

## QA notes
- Product tables identified by toy-number and casting/model-name headers; navigation and collapsible gallery tables excluded.
- Source table and row order retained.
- Raw source headers and cell text/image filenames preserved in the final two columns.
- Matching toy numbers, collection numbers, series labels, body colors, wheel types and notes mapped where source headers support them; remaining fields are retained in raw source data.
- Gallery extraction deferred.

## Output
- `research/extractions/LARGER-SCALE-HOT-WHEELS-XL.csv`
