# Jurassic World Character Cars extraction QA

- Source: `Modern Special Series/Character Cars/Jurassic World Character Cars _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `8dd42f0c56fa9b2a55e1be3cb99b4375193ba355`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 398862
- Fandom revision ID: 688045
- Product tables: 7
- Product rows: 25
- Inline images in product rows: 44
- Links in product rows: 95

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
