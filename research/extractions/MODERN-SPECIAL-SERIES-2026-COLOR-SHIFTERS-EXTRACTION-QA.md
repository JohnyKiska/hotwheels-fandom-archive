# 2026 Color Shifters extraction QA

- Source: `Modern Special Series/Color Shifters/2026 Color Shifters _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `4c34c8390f06fcedafd0c006f2fad94af995aa85`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 368230
- Fandom revision ID: 812864
- Product tables: 2
- Product rows: 26
- Inline images in product rows: 65
- Links in product rows: 137

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
