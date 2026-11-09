# Extraction QA: AcceleRacers Collectible Card Game

- Source: `Modern Special Series/AcceleRacers/AcceleRacers Collectible Card Game _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `b2b64b5ba21cdd4387b21557f345df235c8fb28e`
- Manifest SHA-256: `BACF2491D6BF281774E742BE16BD745ED3193F5DEE3BD54D91A4D9B52F5793EE`
- Source size: 721589 bytes
- HTML content length: 721569 characters
- Fandom revision: not detected
- Product tables extracted: 2
- Product table rows: 279
- Separate Gallery items extracted: 2
- Embedded product-table image references: 554

## Table breakdown

- Table 0: 4 rows, 6 headers; section: Releases[]
- Table 1: 275 rows, 6 headers; section: Cards[]

## QA notes

- Source rows and table boundaries are preserved in source order.
- Original headers, cell HTML, cell text, row HTML, links, and image metadata are retained.
- Repeated labels and identifiers are not merged.
- Tables with fewer than two data rows or navigation-class tables were excluded from product-table extraction; review the source if additional one-off product evidence is present.


## Large-file handling

The complete source extraction is split into six ordered CSV parts to keep each file independently retrievable. Part 01 is the base CSV path; parts 02-06 use the `-PART-NN.csv` suffix. Together they contain all 279 product-table rows and 2 Gallery records in source order.
