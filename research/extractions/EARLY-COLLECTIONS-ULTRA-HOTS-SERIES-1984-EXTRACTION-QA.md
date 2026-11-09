# Ultra Hots Series (1984) extraction QA

- Source: `Early Collections/Ultra Hots Series (1984) _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `63c0056a0bdfeb092efbc49ae1fa5fc1c9e42b73`
- Manifest SHA-256: `F6CDF2E0BAE426690D6989DE58AF92DB73146A79450DBA9EC55B658CA7701C97`
- Source size from MANIFEST: 366,058 bytes; fetched HTML content length: 366,046 characters.
- Fandom revision ID: 742335.

## Extraction

- Product tables: 6.
- Table sections and row counts: 1984 [ ]: 6 rows, 8 columns, 12 embedded images; 1985 [ ]: 7 rows, 8 columns, 14 embedded images; 1986 [ ]: 2 rows, 8 columns, 4 embedded images; Stamper 3-Pack [ ]: 3 rows, 6 columns, 4 embedded images; 4-Pack [ ]: 4 rows, 6 columns, 5 embedded images; Gift Pack [ ]: 4 rows, 6 columns, 5 embedded images.
- Combined product rows: 26.
- Source table schemas are preserved independently. The 1984, 1985 and 1986 tables have Toy # and Country columns; pack tables do not.
- Distinct model-name labels across all tables: 13.
- Toy # values in annual tables: 15 populated cells, 15 distinct values; repeated groups: 0 ().
- Embedded image references: 44, retained per source cell with original image attributes and file links where present.
- Separate standard Wikia gallery items: 0 detected.
- Total CSV records: 26; all records are product_table_row.
- Raw row HTML, source headers, actual source cells, source cell values, source table/row order, section headings, model links and image metadata retained.
- Some pack-table rows have fewer explicit cells because the archived HTML uses row/column spanning. The extractor preserves the actual cells and raw row HTML; it does not pad absent cells with guessed values.
- The Gift Pack table uses the source header `Photo Set`, retained verbatim rather than normalized to `Photo Carded`.

## QA notes

- Repeated names across annual tables and pack tables are distinct source records, not merged.
- No casting/release/package relationships or canonical series hierarchy were inferred beyond the source's own table headings.
