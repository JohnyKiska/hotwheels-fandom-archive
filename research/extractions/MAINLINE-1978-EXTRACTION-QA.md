# Mainline 1978 extraction QA

## Source provenance

- Archive repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Source path: `ALLHW/1978/List of 1978 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `55327b60a4b7d448ef59909aa9d2307925ee8562`
- Git tree file size: 406,167 bytes
- Manifest SHA-256: `e472180afd25cdb4c2d9c20d9be07ecc2391564c21c123cc78fd07e4fb4d1c52`
- Fandom revision: 701293
- Extraction output: `research/extractions/MAINLINE-1978.csv`

## Extraction scope and method

Parsed all three product tables in source order. The fourth table, **Hot Wheels by Year**, is navigation and was excluded. Original table index, section heading, row position, source column count, source headers, and source cell values are retained. A common set of named columns is provided; original headers and row values remain in JSON fields. Missing source fields remain blank. No rows were merged by model name or Toy #.

| Source table index | Section | Source columns | Product rows |
| 0 | 1978 New Releases [ ] | 10 | 12 |
| 1 | 1978 Reissues [ ] | 10 | 38 |
| 2 | Rescue Team [ ] | 9 | 4 |

## Structural QA

- Product tables: 3
- Extracted product rows: 54
- Unique nonblank Toy #: 53
- Blank Toy # rows: 0
- Repeated Toy # groups: 1
- Repeated model-name groups: 1
- Rows with blank Photo: 54
- Collector # column: absent
- Series # column: absent

### Repeated Toy # groups

- `9241`: 2 rows

### Repeated model-name groups

- Corvette Stingray: 2 rows

## Notes

- Rescue Team uses a different first-column header (`Name`); this is retained in raw source fields and mapped to the common Car Name column.
- The three product tables have 9 or 10 columns; the extraction preserves source column counts and does not infer absent attributes.
- Repeated names and Toy # values remain separate source rows. They do not prove casting or release identity.
