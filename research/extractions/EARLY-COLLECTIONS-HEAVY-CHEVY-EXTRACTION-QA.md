# Heavy Chevy extraction QA

## Source provenance
- Repository: `JohnyKiska/hotwheels-fandom-archive`, branch `main`
- Source: `Early Collections/Heavy Chevy _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `1b710580762e9947170e92376c9410c4c8683d92`
- Manifest size: 454,373 bytes
- Manifest SHA-256: `8A478082427112ABDCAAF759187D4D4D799973E821ED61DB3F50F96A3A0A1A76`
- Fandom revision ID: 808320
- Extraction date: 2026-11-09

## Extraction results
- Table 1, section Versions [ ]: 19 product rows, 12 source columns; photo image refs: 19. Headers: Year | Series | Color | Stickers | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 2, section 100% Versions [ ]: 1 product rows, 13 source columns; photo image refs: 1. Headers: Col # | Year | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 3, section Retooled Versions [ ]: 16 product rows, 13 source columns; photo image refs: 16. Headers: Col # | Year | Series | Color | Tampo | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Table 4, section Code 3 [ ]: 8 product rows, 12 source columns; photo image refs: 8. Headers: Year | Series | Color | Tampos | Base Color / / / Type | Window Color | Interior Color | Wheel Type | Toy # | Country | Notes | Photo
- Product rows total: 44
- Separate Gallery entries: 33
- Gallery entries with image filename: 33
- Distinct Toy # values: 18
- Repeated Toy # groups: [["6189",2],["6408",12],["7619",2],["9212",3],["L0737",4]]
- Years present: 1970, 1974, 1976, 1977, 1998, 2002, 2005, 2007, 2008, 2009, 2011, 2013, 2017

## Preservation notes
- Four product tables are retained as separate source tables: Versions, 100% Versions, Retooled Versions and Code 3.
- Original headers and row cell values are preserved in source order. Different source schemas are not forced into a common semantic interpretation.
- Image metadata from individual table cells is retained in the Cell image metadata field. Photo column image filenames, alt text, links and URLs are therefore preserved.
- Gallery entries are exported as separate `gallery_reference` rows, preserving caption, filename, alt, title, file-page link and image URL.
- Repeated Toy # values are not merged. No identity resolution or release/package inference was performed.

## QA
- 44 product rows and 33 separate gallery references exported (77 CSV records total).
- 44 product-photo image refs detected in table rows.
- Source order retained within each table and gallery.

## Output
- `research/extractions/EARLY-COLLECTIONS-HEAVY-CHEVY.csv`
