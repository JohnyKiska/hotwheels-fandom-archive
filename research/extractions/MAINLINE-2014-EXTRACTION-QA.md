# Mainline 2014: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/2014/List of 2014 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `2765d4f199e2fa4552ee059e0bde328d8a8e4463`
- File size: 831,400 bytes
- Manifest SHA-256: `4a1ea5ceb45d424374f3f92f6f78fd40e39b08862e6cd2790f42515647b3c925`
- Fandom revision: 804340

Machine-readable export: [MAINLINE-2014.csv](MAINLINE-2014.csv). It preserves table index, section heading, row order, original column count and raw source headers. Fields are mapped by header name.

## Extraction method

Extracted all 33 product tables separately. The annual Mainline is distributed across 32 series-specific tables. One of these (Batman 75th Anniversary) uses a five-column schema without Series #; the other Mainline tables use six columns. The additional Kroger-exclusive Scavenger Hunt table is kept separate.

## QA results

| Scope | Tables | Rows | Unique Toy # | Collector # |
|---|---:|---:|---:|---:|
| Mainline series tables | 32 | 433 | 433 | 250 numeric values, 001–250 |
| Scavenger Hunt (Kroger Exclusive) | 1 | 4 | 4 | `No #` on all rows |
| Total | 33 | 437 | 437 | 251 distinct raw values including `No #` |

Mainline checks:

- 146 rows marked `(2nd Color)`.
- 15 Treasure Hunt and 15 Super Treasure Hunt rows (Series-label counts).
- No missing values in columns that are actually present in each table.
- The Batman 75th Anniversary table (5 rows) has no Series # column; this is a source schema difference, not missing data.
- 153 Series # cells contain zero-width Unicode characters; these raw characters are preserved in the CSV.
- Photo cells are empty throughout.

Additional section:

- Mission Madness - Scavenger Hunts (Kroger Exclusive): 4 rows, all Collector # = `No #`. Keep this as separate source scope.

## Data-model implications

- Annual Mainline can be split into many series-specific tables, not a single HTML table.
- Source schema may vary between series tables within the same year. Preserve the exact header set per table and map optional fields by header label.
- Do not synthesize Series # for Batman 75th Anniversary.
- Preserve zero-width code points in raw Series #; any normalized value should be derived separately.
- Keep Scavenger Hunt rows separate from numeric Collector # records.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
