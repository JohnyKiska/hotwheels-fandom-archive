# Sizzlers Extraction QA

- Source: `Early Special Series/Sizzlers _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `b7a19948b52818e22a71ce7bc11ddf9e0b0a8af3`
- Source size (bytes): 486564
- Fandom revision ID: not present in source HTML
- Top-level HTML tables scanned: 9
- Product rows extracted: 65
- Embedded table image references: 104
- Links retained from product cells: 246
- Source manifest SHA-256: unavailable in current index/source metadata; left blank in CSV.
- CSV: `research/extractions/EARLY-SPECIAL-SERIES-SIZZLERS.csv`

## Table-level review

| Table | Product rows | Images | Links | Headers |
|---:|---:|---:|---:|---|
| 1 | 8 | 16 | 32 | Toy #; Name; Year; Country; Notes; Photo (Loose); Photo (Sealed) |
| 2 | 8 | 8 | 22 | Toy #; Name; Year; Country; Notes; Photo |
| 3 | 12 | 24 | 48 | Toy #; Name; Year; Country; Notes; Photo (Loose); Photo (Sealed) |
| 4 | 12 | 12 | 25 | Toy #; Name; Year; Country; Notes; Photo |
| 5 | 4 | 8 | 16 | Toy #; Name; Year; Country; Notes; Photo (Loose); Photo (Sealed) |
| 6 | 12 | 24 | 60 | Toy #; Casting; Year; Country; Notes; Photo Loose; Photo Boxed |
| 7 | 4 | 4 | 14 | Toy #; Name; Year; Country; Notes; Photo |
| 8 | 4 | 8 | 20 | Toy #; Casting; Year; Country; Notes; Photo Loose; Photo Boxed |
| 9 | 1 | 0 | 9 | Other Motorized Series |

## Extraction checks

- Rows retained in source order; table/row positions, nearest preceding section heading, headers, raw row HTML, cell HTML/text, links and image metadata preserved.
- Header-only rows excluded, including legacy bold-cell headers.
- Separate product tables retained without merging; no normalization or deduplication.
- Separate gallery entries are not extracted in this pass.
