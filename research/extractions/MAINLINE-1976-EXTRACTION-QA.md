# Mainline 1976 Extraction QA

## Source provenance
- Source: `ALLHW/1976/List of 1976 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Archive branch: `archive/historical-html-1968-2026`
- Git blob SHA: `3bf4b22696cec2d75c2cfe2fe2e8ca7c85160482`
- Git tree size: 405,858 bytes
- Manifest SHA-256: `24e38338b43c096b8e2e6e0ffea9109b4ef3c79b52db88143f8db37a3acce43d`
- Fandom revision: 588485

## Extraction
- One product table, source table index 0.
- One yearly-navigation table was excluded.
- Source headers: Toy #, Casting, Series Name / #, Notes, Wheel Type, Photo.
- Product rows: **41**.
- Source schema: 6 columns for all rows.
- Original row order, source headers and raw cell values retained.

## Identifier and duplicate QA
- Unique nonblank Toy #: **39**.
- Blank Toy #: **1**.
- Repeated Toy # groups: **1** (9203, 2 rows).
- Unique casting names: **40**.
- Repeated casting-name groups: **1** (Mustang Stocker, 2 rows).
- No Collector # or Series # columns.

## Source-specific observations
- Series Name / # values occur as 1976 Flying Colors (30 rows), Super Chromes (9 rows), and Flying Colors (2 rows). These exact labels are retained without taxonomy normalization.
- Two Notes cells contain source descriptions: Emergency Squad, "Gray tinted windows"; Mercedes-Benz C-111, "Black Plastic base".
- All Wheel Type and Photo cells are blank.
- One row has a blank Toy # and remains preserved.
- Duplicate Toy # and casting-name entries remain separate source rows and are not interpreted as proof of release or casting identity.

## Output
- `research/extractions/MAINLINE-1976.csv`
- `research/extractions/MAINLINE-1976-EXTRACTION-QA.md`
