# Mainline 1974 Extraction QA

## Source and provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Source path: `ALLHW/1974/List of 1974 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `698d9da70600e058cab0a63881daa52eee809f54`
- Git tree / Contents API size: 382,121 bytes
- Manifest SHA-256: `592dfebd1c7a56812465defe563fc96a3d6ba1542eecf8833b00c71e36f42765`
- Fandom revision: 717416

## Extraction result

- HTML tables found: 2
- Product tables extracted: 1 (table index 0)
- Navigation table excluded: table index 1
- Source columns: Toy # | Casting | Series Name | Notes | Wheel Type | Photo / Color
- Extracted product rows: 25
- Source column count observed: 6
- Unique nonblank Toy #: 25
- Blank Toy #: 0
- Repeated Toy # groups: 0
- Unique casting names: 25
- Repeated casting-name groups: 0
- Collector # / Series # columns: absent
- Series values: `1974 Flying Colors` (24), `Mountain Mining Set` (1)
- Nonblank Notes: `Baja Bruiser`: NEW!; `Breakaway Bucket`: NEW!; `El Rey Special`: NEW!; `Rodger Dodger`: NEW!; `Steam Roller`: NEW!; `Sir Rodney Roadster`: NEW!; `Road King Truck`: NEW!
- Wheel Type image metadata: 25 rows; labels: `Redline2 - 6164bf` (25)
- Photo image metadata: 25 rows

## Structural observations

The page contains one six-column product table and one yearly-navigation table. The product table's Wheel Type and Photo cells are image-only; visible cell text is empty. Image `alt` labels and `data-image-name` filenames were decoded and captured into the export fields.

All 25 Wheel Type cells use the same image label, `Redline2 - 6164bf`. All 25 rows have Photo image metadata. Photo labels / filenames are retained as source metadata, not interpreted as verified color or release attributes.

The table contains 24 rows assigned to `1974 Flying Colors` and one row, `Road King Truck`, assigned to `Mountain Mining Set`. This distinct source series value is preserved as-is rather than being forced into Flying Colors.

Seven Notes cells contain `NEW!`: Baja Bruiser, Breakaway Bucket, El Rey Special, Rodger Dodger, Steam Roller, Sir Rodney Roadster, and Road King Truck. These notes are source annotations, not normalized release statuses.

## Duplicate and identifier checks

- Repeated Toy # groups: none.
- Repeated casting-name groups: none.
- No rows were deduplicated or merged.

## Output

- `research/extractions/MAINLINE-1974.csv`
- `research/extractions/MAINLINE-1974-EXTRACTION-QA.md`

All 25 product rows are retained in source order. Raw source headers and per-cell text/image metadata are included in the CSV.
