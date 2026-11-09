# Action Command extraction QA

## Source
- Archive repository: `JohnyKiska/hotwheels-fandom-archive`
- Branch: `main`
- Source path: `Early Collections/Action Command _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `aac8bef248329166dd47ca7387d31dd6a89c3b1d`
- File size from MANIFEST.csv: 369,285 bytes
- Manifest SHA-256: `85E2322618CE94656A090644CD477C0613E2931791FEC17479155CD2DF2B4F85`
- Fandom revision ID: 761080
- Extraction date: 2026-11-09
- Scope: all product tables on the archived page; no cross-source enrichment.

## Extraction results
- Product tables: 2
- Original Card: 8 data rows, 10 source columns.
- 1987-1989 Card: 30 data rows, 10 source columns.
- Total product rows: 38
- Unique model names: 13
- Distinct Toy # values: 13
- Year values: 1985, 1986, 1987, 1988, 1989
- Rows with loose-photo filenames: 38 / 38
- Rows with carded-photo filenames: 38 / 38
- Repeated Toy # groups: 13
  - 2518: 2 rows
  - 2519: 3 rows
  - 3338: 2 rows
  - 4059: 4 rows
  - 5022: 3 rows
  - 5025: 4 rows
  - 9371: 3 rows
  - 9372: 3 rows
  - 9373: 2 rows
  - 9374: 3 rows
  - 9375: 4 rows
  - 9379: 3 rows
  - 9380: 2 rows

## Preservation and QA
- Original table boundaries and section headings are retained.
- Row positions are 1-based within each source table, excluding the header row.
- Original column names are retained in `Raw source headers`.
- Each row's normalized visible cell text and image filename/alt label are retained in `Raw source cells`.
- Loose and carded photo filenames are extracted separately; URLs are not inferred.
- All 38 source rows are retained. Repeated Toy # values remain separate rows.
- No automatic merging by Toy #, model name, year, or color was performed.

## Interpretation cautions
- The page describes Action Command as a military-themed series released between 1985 and 1989.
- “Original Card” and “1987-1989 Card” are the page's own section headings. They are retained as source groupings, not promoted to canonical release taxonomy.
- Repeated Toy # values occur across multiple source rows, often with differing year/color data. These are not presumed to be errors or identical physical releases.
- No casting identity, release chronology, regional scope, or tooling lineage has been independently resolved.

## Output
- `research/extractions/EARLY-COLLECTIONS-ACTION-COMMAND.csv`
