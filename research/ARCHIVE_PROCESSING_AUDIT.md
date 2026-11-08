# Archive Processing Audit: Mainline (2026-11-08)

## Scope and method

This audit compares the committed Git trees of the two archive repositories with the current research index and findings. It distinguishes source availability from page review, row extraction, QA, and database-ready normalization.

Repositories and immutable tree snapshots inspected:

- Mainline archive: `JohnyKiska/hotwheels`, branch `archive/historical-html-1968-2026`, commit `2f43ad43324c6a16c786dad4b34fceac7693e5d6`, tree `6e1b4df82f50e4bfb7ab7186164b96422e4387b9`.
- Fandom archive: `JohnyKiska/hotwheels-fandom-archive`, branch `main`, commit `620654d5c1698c3114c880e915589780781d02f7`, tree `4a480a2909d76753a8b07a94347607a2fec200e5`.
- Mainline manifest: `ALLHW/MANIFEST.csv`, blob `1a5933422177fa94fb09b1e9357e3a41c37094d6`.

The inventory is based on the recursive Git tree and manifest, not on assumptions from local folder names.

## 1. Source inventory: Mainline

The `ALLHW/` directory contains:

- 59 year directories, 1968 through 2026 inclusive, with no missing year directory.
- 60 HTML pages: one annual page for every year plus a second 2010 International page.
- `MANIFEST.csv` contains 60 data records (61 lines including header), matching the 60 HTML pages.
- The 2010 ordinary and International pages are separate source datasets and must not be merged without comparison.

The Fandom archive repository separately contains 530 HTML/HTM files and 2 CSV files (532 files total), matching the previously recorded inventory. This is a separate collection from the 60-page Mainline `ALLHW/` dataset.

## 2. Mainline processing status

Status labels:

- **Extracted + QA**: full table extraction and explicit row/identifier checks documented.
- **Partial anchor**: used as a comparison source or reviewed selectively, but no complete annual extraction/QA is documented.
- **Not yet audited**: source exists, but current research documentation contains no evidence of a systematic annual-page extraction and QA.
- **Special handling required**: separate source variant must be compared independently.

| Year/source | Archive status | Research status | Audit conclusion |
|---|---|---|---|
| 1968–2009 (42 annual pages) | Present | No complete year-by-year extraction/QA documented in current research index | Not yet audited as annual Mainline datasets |
| 2010 ordinary | Present | No independent full extraction/QA documented | Special handling required |
| 2010 International | Present | No independent full extraction/QA documented | Special handling required; compare against ordinary 2010 |
| 2011–2023 (13 annual pages) | Present | No complete year-by-year extraction/QA documented | Not yet audited as annual Mainline datasets |
| 2024 | Present | Full table re-extracted and QA checked: 441 rows, 441 unique Toy #, 250 Collector #, 132 rows marked (2nd Color), 15 TH + 15 STH; 49 prior Car Culture name-match candidates remain unadjudicated | Extracted + QA |
| 2025 | Present | Full extraction and QA documented: 440 rows, 440 unique Toy #, 250 Collector #, 146 rows marked (2nd Color); Premium comparisons completed | Extracted + QA |
| 2026 | Present | No complete annual extraction/QA documented in current research index | Not yet audited |

**Important qualification:** “Not yet audited” means the current research documentation does not demonstrate a complete annual extraction and QA. It does not mean nobody has ever opened or inspected the page. Research of individual castings/series elsewhere in the archive does not count as extraction of the corresponding annual Mainline list.

### 2025 verified extraction

Source: `ALLHW/2025/List of 2025 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`

- Git blob SHA: `b155324bd3fca3281ed91fd7a8fa992e04f1662f`
- File size: 824,886 bytes
- Manifest SHA-256: `bbdac9d328130734328c1bb9b8a01fc738055dd596f0b7dfcf286ae5b142672c`
- Extracted rows: 440
- Unique Toy #: 440
- Unique Collector #: 250
- Rows marked `(2nd Color)`: 146

Detailed extraction QA and Mainline/Premium candidate comparisons are recorded in `research/comparisons/MAINLINE-PREMIUM-2025.md`.

### 2024 extraction status

The 2024 annual list has now been re-extracted from the canonical archive branch and passed structural QA. Results, provenance, and the machine-readable row export are recorded in `research/extractions/MAINLINE-2024-EXTRACTION-QA.md` and `research/extractions/MAINLINE-2024.csv`. The prior 49 Car Culture exact-name matches remain candidate links only; they still require row-level adjudication for casting/tooling identity.

## 3. Mainline work remaining

Priority order:

1. Adjudicate the existing 49 Car Culture ↔ Mainline 2024 name-match candidates against the newly QA-checked canonical 2024 extraction. Preserve the comparison as a separate run.
2. Process 2010 ordinary and International independently. Compare their row counts, identifiers, model names, regional differences, and overlaps; do not deduplicate automatically.
3. Extract and QA 1968–2009 annual pages, preserving original table boundaries, row order, raw identifiers, color/series notes, and any non-table sections.
4. Extract and QA 2011–2023 annual pages with the same method.
5. Extract and QA 2026, keeping announced/planned entries distinct from confirmed releases where the source indicates uncertainty.
6. Build year-scoped cross-program comparisons only after each annual Mainline source has a verified extraction. Do not infer a match in another year from the 2024/2025 samples.

For every annual page, record source path, branch, Git blob SHA, manifest SHA-256, Fandom revision/date if available, extraction method/version, table boundaries, row counts, unique identifier counts, duplicate groups, and unresolved anomalies.

## 4. Data-model and QA cautions

- Mainline Toy # and Collector # are different identifier namespaces. Collector # is not a unique release key: regular and STH rows may share it.
- Color variants can have distinct Toy # while sharing Collector #; preserve raw labels such as `(2nd Color)`.
- Keep annual list row identity separate from casting identity and from the physical release/product identity.
- Treat regional/international lists as separate source scopes until compared.
- Do not treat the annual page's row count as the number of unique castings.
- Keep source assertions and uncertainty explicit; exact name matches do not prove casting/tooling identity.

## 5. Archive-wide inventory checkpoint

The Fandom archive tree currently contains 530 HTML/HTM files and 2 CSV files. This audit does not yet assign a final processing status to every Fandom HTML page. That is the next inventory phase, after Mainline. The planned next scope is Early Collections, Early Special Series, Other Early Series, then the remaining modern categories. Folder taxonomy is an archival organization, not a verified product hierarchy.
