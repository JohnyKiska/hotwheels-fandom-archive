# Pro Racing 1:43 Scale extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Larger Scale/Pro Racing 1_43 Scale _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `68a81db768774244b3f0cfb1ec1d0acf5b4213b3`
- Manifest file size: 458813 bytes
- Manifest SHA-256: `6D139E731962E0CB46702A3E679510A3A0DA75974C0B11CA93E21E6AC906C949`
- Fandom revision ID: 815866
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 41
- Export columns: 21
- Other HTML tables excluded: 1

## Product tables
- Vehicles: 41 rows, 11 source columns. Headers: Casting | Year | Color | Tampo | Base Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo

## QA notes
- Product tables identified by toy-number and casting/model/name headers; navigation and collapsible gallery tables excluded.
- Source table and row order retained.
- Raw source headers and cell text/image filenames preserved in the final two columns.
- Matching toy numbers, collection numbers, year, series labels, body colors, wheel types, country and notes mapped where source headers support them; remaining fields are retained in raw source data.
- Gallery extraction deferred.

## Output
- `research/extractions/LARGER-SCALE-PRO-RACING-1-43-SCALE.csv`
