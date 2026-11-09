# 2018 Color Shifters extraction QA

- Source: `Modern Special Series/Color Shifters/2018 Color Shifters _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `84f4fe9170931f6a9d8245382e785e558d475996`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 345825
- Fandom revision ID: 781197
- Product tables: 2
- Product rows: 20
- Inline images in product rows: 36
- Links in product rows: 91

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
