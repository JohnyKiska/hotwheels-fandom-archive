# Trailbusters extraction QA

- Source: `Early Collections/Trailbusters _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `f35ce4e7cbf57e651d6fa0badfa56f4ae9872811`
- Manifest SHA-256: `64C7037EFB58AEB1E93D8ED704262DA7E87AB149F4CB4AD77EE0EC22D90F3B4A`
- Source size from MANIFEST: 395,265 bytes; fetched HTML content length: 395,251 characters.
- Fandom revision ID: 763267.

## Extraction

- Product tables: 1.
- Table 1: one unheaded article table, 49 data rows, 9 source columns.
- Source headers: Toy #, Model Name, Color, Year, Wheel Type, Country, Notes, Photo Loose, Photo Carded.
- Product rows: 49; distinct Model Name labels: 15.
- Toy # values: 49 populated cells, 18 distinct values, no empty cells.
- Repeated Toy # groups: 17. Values and row counts: `1470` (5), `1516` (4), `1517` (2), `1520` (4), `2534` (3), `2539` (2), `2541` (2), `2542` (2), `3209` (2), `3716` (2), `4360` (4), `4361` (3), `4392` (3), `5113` (2), `5146` (2), `5910` (2), `7530` (4).
- Repeated names and Toy # values remain separate source records; no rows were merged.
- Embedded product-table image references: 97 (48 in Photo Loose; 49 in Photo Carded).
- Empty cells by source column: Toy #: 0; Model Name: 0; Color: 0; Year: 0; Wheel Type: 0; Country: 0; Notes: 32; Photo Loose: 49; Photo Carded: 49.
- Separate standard Wikia gallery items: 0 detected. No gallery records were fabricated.
- Total CSV records: 49; all records are product_table_row.
- Raw source headers, raw cell HTML, decoded source cell values, source order, table/row indices, internal model links and per-cell image metadata retained.

## Notes

- The article's product table has no preceding section heading in the archived article body; it is labelled `Unheaded article table` to preserve that source context rather than inventing a section name.
- All 49 source rows are preserved individually, including country-specific and wheel-type variants.
- Photo Loose and Photo Carded cells contain image references in every row (97 references total); these are retained in cell-level image metadata.
- No release, casting, package or series hierarchy was inferred beyond the source's own labels.
