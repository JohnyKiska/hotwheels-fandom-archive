# HW Racing Series (2012) extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Larger Scale/Hot Wheels Racing Series/HW Racing Series (2012) _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `702f0c998b97011bf1f16e93b5d78f09b5975a9e`
- Manifest file size: 334961 bytes
- Manifest SHA-256: `034096C37D0E155C9037D568D76B3C3C422CEEA79CAD35F5BCA02CEF6AFD677E`
- Fandom revision ID: 631869
- Extraction date: 2026-11-09

## Extraction results
- Product tables: 1
- Product rows: 22
- Export columns: 21
- Other HTML tables excluded: 0

## Product tables
- HW Racing Series (2012): 22 rows, 6 source columns. Headers: Toy # | Col. # | Casting | Series | Series # | Photo

## QA notes
- Product tables identified by toy-number and casting/model-name headers; navigation and collapsible gallery tables excluded.
- Source table and row order retained.
- Raw source headers and cell text/image filenames preserved in the final two columns.
- Matching toy numbers, collection numbers, series labels, body colors, wheel types and notes mapped where source headers support them; remaining fields are retained in raw source data.
- Gallery extraction deferred.

## Output
- `research/extractions/LARGER-SCALE-HW-RACING-SERIES-2012.csv`
