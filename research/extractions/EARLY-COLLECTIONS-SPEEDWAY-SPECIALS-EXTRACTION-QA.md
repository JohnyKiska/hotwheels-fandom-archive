# Speedway Specials extraction QA

- Source: `Early Collections/Speedway Specials _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `de473d47ac484f9feb903c8448b23794d6052eaf`
- Manifest SHA-256: `E13939B15DA60B1312CF23E964B46B3DD8BCA6636A305CBD5833E719C49EBF0D`
- Source size from MANIFEST: 352,847 bytes; fetched HTML content length: 352,837 characters.
- Fandom revision ID: 767746.
- Article introduction states that Speedway Specials was one of seven Patch Card themes, produced in 1978 and 1979 in Hong Kong; six proofs of purchase and 25 cents postage/handling were required to mail for a patch. The table itself has no Year column.

## Extraction
- Product tables: 1, Article main table (introductory prose; no section heading), 17 data rows, 9 source columns (Toy #, Collector #, Vehicle Name, Color, Tampo, Wheel Type, Notes, Photo Loose, Photo Carded).
- Separate standard Wikia gallery items: 2.
- Total CSV records: 19.
- Images embedded in product-table cells: 34; unique gallery image assets: 3. Gallery markup repeats image elements in noscript/lazy-load forms; raw references are retained.
- All 17 product rows have Toy # and Collector # fields. Toy # values: 14 distinct; repeated values: `17` (2), `21` (2), `38` (2).
- Vehicle-name labels: 15 distinct; repeated labels: `Monte Carlo Stocker` (2), `Torino Stocker` (2).
- Raw source headers, cell values and HTML, source row order, model links, and per-cell image metadata (alt, filename, image key, src/data-src, dimensions) retained. Repeated identifiers and labels are preserved as separate rows.

## Gallery
- Item 1: filename `PATCH SPEEDWAY SPECIALS Formula 5000 b.jpg`; alt `Mail-Away PATCH SPEEDWAY SPECIALS`; file link `/wiki/File:PATCH_SPEEDWAY_SPECIALS_Formula_5000_b.jpg`.
- Item 2: filename `Back of Patch Card.jpg`; alt `Back of Patch Cards`; file link `/wiki/File:Back_of_Patch_Card.jpg`.

## Notes
- Repeated Toy # groups and vehicle-name labels are not deduplicated. No individual release years are inferred from article categories or introductory prose.
- CSV records retain full raw source row/cell HTML and source-specific image/link references.

## Output
- `research/extractions/EARLY-COLLECTIONS-SPEEDWAY-SPECIALS.csv`
