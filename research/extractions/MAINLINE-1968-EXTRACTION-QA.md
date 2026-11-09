# Mainline 1968 Extraction QA

## Source
- Archive path: `ALLHW/1968/List of 1968 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `c7059a95219d5c8c68136cddaa128f0fd1854d3c`
- Git tree / Contents API size: 391,598 bytes
- Manifest SHA-256: `57fe1c9de77bc4bf9c8c98254087ab625e266c67e69943a70aa156826bfa48f2`
- Fandom revision: 807771

## Extraction
- Product tables: 1
- Product rows: 16
- Product table heading: 1968 Hot Wheels
- Gallery sections: 1
- Gallery entries: 26
- Total CSV data rows: 42
- Product table headers: ["Toy #","Model Name","Photo"]
- Unique nonblank Toy #: 16
- Blank Toy #: 0
- Repeated Toy # groups: []
- Unique model names: 16
- Repeated model-name groups: []
- Product rows preserve source order, Toy #, model-page link, image filename and alt metadata where available.
- Gallery contains 26 entries: two general historical images, one 1968 International Collector's Catalogue cover, and 23 catalogue page images. The 23 page images have blank source captions; filenames are retained and captions are not inferred.
- No structured color/tampo/base/window/interior/wheel/country attributes in the product table; these fields remain blank.
- Gallery entries are kept separate from product rows and are not interpreted as castings.

## QA notes
- Yearly navigation table excluded.
- All 16 product rows extracted from the single product table.
- Original source headers, raw cell text, row positions, image filenames, alt labels and links retained.
- Blank gallery captions are intentional source blanks, not missing extraction.
