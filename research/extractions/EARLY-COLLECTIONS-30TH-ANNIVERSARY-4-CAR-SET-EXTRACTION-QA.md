# Hot Wheels 30th Anniversary 4-Car Set extraction QA

## Source provenance
- Source: `Early Collections/Hot Wheels 30th Anniversary 4-Car Set _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `b278df831c1539c16f123cf442511afe4892015e`
- Manifest size: 326,597 bytes
- Manifest SHA-256: `1A7A32445EFD2DD2A1C54EF53D7ACFFB4B7549C92C59B41666162B6A464B3623`
- Fandom revision ID: 805834
- Extraction date: 2026-11-09

## Extraction results
- Conventional product tables: 1
- Product rows: 4
- Source columns: 11
- Table header labels: Year, Model, Color, Tampo, Base Color / / / Type, Window Color, Interior Color, Wheel Type, Toy #, Notes / / / Variations, Photo
- Separate gallery entries: 0
- Vehicle names: Nitty Gritty Kitty; Heavy Chevy; King 'Kuda; Light My Firebird
- Source Year-column value: 19322 (one rowspan=4 cell shared by all four rows)
- Toy # values: 19322
- Photo references: 4
- Rows retained: 4

## Important source observations
- The first source header is literally `Year`, but its only value is `19322` in a cell with `rowspan="4"`. This value is preserved verbatim and is not interpreted as a calendar year.
- The table also has a separate `Toy #` column, where all four rows show `19322`.
- The first cell's rowspan applies to all four vehicles. The CSV records this inherited source context explicitly for rows 2–4 rather than fabricating repeated raw cells.
- The four models are retained as separate product-table rows: Nitty Gritty Kitty, Heavy Chevy, King 'Kuda, Light My Firebird.
- Photo image metadata and model links are retained. No year or individual release/package facts were inferred.
- The page title identifies a 4-Car Set; the table lists four vehicle entries. No additional contents were invented.

## QA
- All 4 rows retained in source order.
- Raw source headers and raw source cell HTML retained.
- Rowspan semantics explicitly documented.
- No deduplication by Toy #, model, or shared set number.

## Output
- `research/extractions/EARLY-COLLECTIONS-30TH-ANNIVERSARY-4-CAR-SET.csv`

## CSV audit correction (2026-11-09)
- The initial CSV export contained one surplus empty field immediately before `Photo filename` in each of the four product rows. This shifted the photo filename, alt text, URL, and trailing provenance fields one column to the right.
- Removed only that surplus empty field from each affected row. All four rows now match the 20-column header; product values, raw source cells, rowspan context, and cell links were preserved.
- The source photo URL cells for King 'Kuda and Light My Firebird still contain lazy-load `data:image/gif` placeholders; their real `data-src` URLs remain present in the raw source HTML. This is recorded for the later Gallery extraction/image URL pass, not silently rewritten during this structural correction.
