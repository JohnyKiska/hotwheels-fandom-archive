# Shift Kickers Extraction QA

- Source: `Early Special Series/Shift Kickers _ Hot Wheels Wiki _ Fandom.html`
- Source blob SHA: `39a382a2829e7cf7c1b7e0353957b042aea03ba0`
- Source size (bytes): 322655
- Fandom revision ID: not present in source HTML
- Top-level HTML tables scanned: 1
- Product rows extracted: 6
- Embedded table image references: 6
- Links retained from product cells: 18
- Source manifest SHA-256: unavailable in current index/source metadata; left blank in CSV.
- CSV: `research/extractions/EARLY-SPECIAL-SERIES-SHIFT-KICKERS.csv`

## Table-level review

| Table | Product rows | Images | Links | Headers |
|---:|---:|---:|---:|---|
| 1 | 6 | 6 | 18 | Year; Model name; Series; Color; Tampo; Base Color / Type; Window Color; Interior Color; Wheel Type; Country; Number; Photo |

## Extraction checks

- Rows retained in source order; table/row positions, nearest preceding section heading, headers, raw row HTML, cell HTML/text, links and image metadata preserved.
- Header-only rows excluded, including legacy bold-cell headers.
- Separate product tables retained without merging; no normalization or deduplication.
- Separate gallery entries are not extracted in this pass.
