# HiRakers extraction QA

## Source provenance
- Source: `Early Collections/HiRakers _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `15ce02f85796913b6b1cd9f27b66348f9416e18e`
- Manifest size: 354,036 bytes
- Manifest SHA-256: `071EB7131AACB81DEE42E1AFF777F64D523B1C516810A751885B1AA82CAD5D9A`
- Fandom revision ID: 798213
- Extraction date: 2026-11-09

## Extraction results
- Conventional product tables: 1
- Product rows: 16
- Source columns: 10 (Toy #, Model Name, Color, Year, Tampo, Wheel Type, Country, Notes, Photo Loose, Photo Carded)
- Additional gallery references: 2
- Total CSV records: 18
- Years present in table: 1980, 1981, 1982, 1983, 1984
- Distinct model names: 6
- Distinct Toy # values: 7
- Image references in product cells: 32
- Gallery image references: 2
- Blank Toy # values: 0
- Repeated Toy # groups: 1131 (4 rows), 1132 (2 rows), 1133 (2 rows), 1134 (2 rows), 1135 (2 rows), 1136 (3 rows)
- Repeated model groups: 3-Window '34 (2 rows), 40's Woodie (4 rows), Dodge D-50 (2 rows), Split Window '63 (4 rows), Turbo Wedge (2 rows), 'Vette Van (2 rows)

## Important source observations
- The introductory text describes the original HiRakers from 1980 to 1984 and separately mentions a 2006 revival. The table itself contains 16 rows across 1980, 1981, 1982, 1983, 1984.
- Original Toy # and model rows are preserved individually. Repeated Toy # values represent multiple source records and were not merged.
- The table's Photo Loose and Photo Carded cells contain images rather than textual values. Their filenames, alt labels, URLs and image keys are retained in cell-level metadata.
- `Image Not Available.jpg` entries are retained as source data, not treated as missing rows.
- Two additional gallery items are preserved separately, including a card image and a back-of-card image.
- No package/release identity or extra year was inferred from image filenames.

## QA
- 16 product table rows retained in source order.
- 2 gallery entries retained separately.
- Raw source headers, raw source cells, image metadata and links are included in CSV.
- No deduplication or normalization of repeated Toy # records.

## Output
- `research/extractions/EARLY-COLLECTIONS-HIRAKERS.csv`
