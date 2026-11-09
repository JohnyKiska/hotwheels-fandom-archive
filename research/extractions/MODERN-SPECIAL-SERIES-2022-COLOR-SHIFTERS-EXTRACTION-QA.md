# 2022 Color Shifters extraction QA

- Source: `Modern Special Series/Color Shifters/2022 Color Shifters _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `35fe9fbcd5dba4623d1990c478ab6fedd9fa9dff`
- Manifest SHA-256: ``
- Source size (bytes, Manifest): 
- Fetched HTML length (characters): 351589
- Fandom revision ID: 781194
- Product tables: 2
- Product rows: 23
- Inline images in product rows: 43
- Links in product rows: 83

## Extraction method

- Parsed archived HTML directly; retained each raw product row HTML.
- Preserved table headers, cell HTML/text/attributes, links, and image attributes in structured JSON columns.
- Excluded the navigation table titled `Yearly Lists of Basic Line and Other collections`.
- Gallery-only items are not extracted in this pass and remain a follow-up task.
- CSV schema: 21 columns; one record per product row.

## QA notes

- Counts are mechanical extraction counts; product identities have not yet been normalized.
- Gallery content and downstream normalization remain separate review tasks.
