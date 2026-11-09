# Mainline 1969 Extraction QA

## Source
- Archive path: `ALLHW/1969/List of 1969 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `0025ba6f145c3c7e0a891a37d3c35610ddedcdc2`
- Git tree / Contents API size: 372,235 bytes
- Manifest SHA-256: `e6f2bbe1f08d6ad049b568072c533f7d765312cf6d5d2cace12e31995261832d`
- Fandom revision: 751481

## Extraction
- Product tables: 2
- Product rows: 24
- Table 1, 1969 Hot Wheels: 16 rows.
- Table 2, Exclusive Grand Prix: 8 rows.
- Gallery sections: 1
- Gallery entries: 1
- Total CSV data rows: 25
- Source table headers: Toy #, Model Name, Photo.
- Unique nonblank Toy #: 24
- Blank Toy #: 0
- Repeated Toy # groups: []
- Unique model names: 24
- Repeated model-name groups: []
- Structured release attributes (color/tampo/base/window/interior/wheel/country): absent from source tables; left blank.
- Photo filenames, alt labels, model-page links and image-file links retained in raw source cells.
- Gallery caption, alt, filename and file link retained separately.
- Cross-listed castings are not deduplicated. Table membership remains part of each source record.

## QA notes
- Yearly navigation table excluded.
- Both product tables extracted independently in source order.
- Gallery image is retained separately and is not counted as a casting.
- Original headers, source cell values, row positions and table boundaries preserved.
