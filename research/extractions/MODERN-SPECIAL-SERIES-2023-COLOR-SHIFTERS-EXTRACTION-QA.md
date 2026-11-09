# 2023 Color Shifters extraction QA

- Source: `Modern Special Series/Color Shifters/2023 Color Shifters _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `d33b643b9081f913a0aaacbf91c3caa1a6568165`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 346264
- Fandom revision ID: 781200
- Product tables: 2
- Product rows: 21
- Inline images in product rows: 38
- Links in product rows: 76

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
