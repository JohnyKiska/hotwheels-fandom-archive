# Mainline 1979 extraction QA

## Source provenance

- Archive repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Source path: `ALLHW/1979/List of 1979 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `446a651ba72ec88ea4ffaea5b4b941626db15b4c`
- Git tree file size: 406,065 bytes
- Manifest SHA-256: `470afdee16fd79b22e625f0b4b8a6d75b7ebb7bd7a2bb26d1c2bd3092edf6bf8`
- Fandom revision: 666008
- Extraction output: `research/extractions/MAINLINE-1979.csv`

## Extraction scope and method

Parsed all six product tables in source order. The seventh table, **Hot Wheels by Year**, is navigation and was excluded. Original table index, section heading, row position, source column count, source headers, and source cell values are retained. The export uses a common set of named columns while preserving each source row's original headers and values in JSON fields. Missing source fields remain blank; rows are not merged by model name or Toy #.

| Source table index | Section | Source columns | Product rows |
| 0 | New Castings [ ] | 10 | 12 |
| 1 | Repaints and Base Changes [ ] | 10 | 20 |
| 2 | Golden Machines 6-Pack [ ] | 10 | 6 |
| 3 | The Heroes [ ] | 9 | 6 |
| 4 | Scene Machines [ ] | 9 | 6 |
| 5 | Rescue Team [ ] | 9 | 1 |

## Structural QA

- Product tables: 6
- Extracted product rows: 51
- Unique nonblank Toy #: 46
- Blank Toy # rows: 4
- Repeated Toy # groups: 1
- Repeated model-name groups: 9
- Rows with blank Photo: 51
- Collector # column: absent
- Series # column: absent

### Repeated Toy # groups

- `7660`: 2 rows

### Repeated model-name groups

- Inside Story: 2 rows
- Monte Carlo Stocker: 2 rows
- GMC Motorhome: 2 rows
- Letter Getter: 3 rows
- Corvette Stingray: 2 rows
- Super Van: 2 rows
- Army Funny Car: 2 rows
- Hot Bird: 2 rows
- Spoiler Sport: 2 rows

## Notes

- The Heroes table uses `Original Casting` and `Series Rename`; these values are retained in the normalized Car Name and Series columns while the raw source headers/cells preserve the original representation.
- Rescue Team is a one-row table with a different source header (`Name`).
- Source table schemas vary (including 9- and 10-column tables); no missing fields were inferred.
- Repeated names and Toy # values are retained as separate source rows. They are not evidence by themselves of identical castings or releases.
