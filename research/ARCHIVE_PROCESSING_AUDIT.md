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
| 1968–1978 (11 annual pages) | Present | No complete year-by-year extraction/QA documented | Not yet audited as annual Mainline datasets |
| 1979 | Present | Extracted 51 rows from 6 product tables; 46 unique nonblank Toy #, 4 blank Toy #; 1 repeated Toy # groups and 9 repeated model-name groups. Seven-column? Structural variation retained; no Collector # or Series #. | Extracted + QA |
| 1980 | Present | 49 rows across 2 product tables; 42 unique nonblank Toy #; 3 blank Toy #; 4 repeated Toy # groups; 3 repeated casting-name groups | Extracted + QA |
| 1981 | Present | 27 rows across New Castings, Repaints, Scene Machines and Heroes; 23 unique nonblank Toy #; 1 blank Toy #; repeated Toy # and names preserved; no Collector # or Series #; Heroes has Original Casting/Year/Series Rename schema | Extracted + QA; source-specific schema and identifier collision flagged |
| 1982 | Present | 90 rows across New Castings, Reissues, Megaforce Series, HiRakers and Workhorses; 74 unique nonblank Toy #; 9 blank Toy #; repeated identifiers and names preserved; no Collector # or Series # | Extracted + QA; table schema differences and identifier collisions flagged |
| 1983 | Present | 67 rows across New Castings, Real Riders, Reissues, Extras Series and HiRakers; 51 unique nonblank Toy #; 7 blank Toy #; repeated identifiers and names preserved; no Collector # or Series # | Extracted + QA; source-table differences and identifier collisions flagged |
| 1984 | Present | 35 rows across New Castings, Real Riders, Ultra Hots and Reissues; 12-column and 11-column schemas; repeated Toy # 7293 in two Flame Runner variants; blank Toy # values retained | Extracted + QA; repeated identifiers and historical notes flagged |
| 1985 | Present | 38 rows across New Castings, Real Riders, Ultra Hots and Reissues; no Collector # or Series # columns; 12-column and 11-column schemas; blank Toy # values and repeated casting names preserved | Extracted + QA; source-scope variants and historical notes flagged |
| 1986 | Present | 26 rows across New Castings, Reissues and Real Riders; 20 unique Toy #; country and set-only qualifiers preserved | Extracted + QA; repeated Toy # and scope collisions flagged |
| 1987 | Present | 23 rows across New Castings, Reissues and Real Riders; 20 unique Toy #; no Collector # field | Extracted + QA; repeated Toy # variants flagged |
| 1988 | Present | 27 rows across New Castings and Reissues; 25 unique Toy #; no Collector # field; two Toy # values have two color variants each | Extracted + QA |
| 1989 | Present | One five-column annual table; 76 rows, Col. #001–076 and Series #1/76–76/76; no Toy # field | Extracted + QA |
| 1990 | Present | 87 rows across New Castings, Reissues, The Simpsons and California Customs; only New Castings has Collector # | Extracted + QA; repeated Toy # and blank Toy # rows flagged |
| 1991 | Present | 62 rows across New Castings, Reissues and California Customs; California Customs has separate no-Collector-# scope | Extracted + QA; blank and repeated identifiers flagged |
| 1992 | Present | 24 rows across New Castings, Reissues and Gleam Team; two source schemas; two Gleam Team Toy # values blank | Extracted + QA |
| 1993 | Present | 72 rows across five tables with distinct schemas; New Castings/Reissues, Tattoo Machines, Demolition Man and 25th Anniversary Series retain separate identifiers | Extracted + QA; duplicate/conflicting IDs and blanks flagged |
| 1994 | Present | 14 rows across two 12-column tables (New Models and Reissues); preserves detailed color, tampo, base/window/interior, wheel and Toy # fields | Extracted + QA; missing and suspicious fields flagged |
| 1995 | Present | 97 rows across 15 tables; 97 unique Toy # and Collector #; 12 Treasure Hunts; 1995 Hot Wheels has 7-column schema with Color and Rims | Extracted + QA |
| 1996 | Present | 141 rows across 17 product tables; 136 unique Toy # and Collector # values; two exact duplicate rows in 1996 Hot Wheels; 64-row five-column table omits Series # | Extracted + QA; duplicate rows and cross-scope Toy # collisions flagged |
| 1997 | Present | Numbered list: 119 rows, numeric Collector #147–642 (non-dense); Bonus Cars 4 rows (#001–004); seven other series tables: 28 rows with Collector # = N/A | Extracted + QA |
| 1998 | Present | 185 numbered-list rows, 184 unique Collector # values across 633–908; one repeated #780/Toy #19949 row; separate Bonus Cars 4 rows | Extracted + QA |
| 1999 | Present | 196 numbered-list rows with Collector #649–1121 (non-dense); separate Final Run (12 rows, Collector # blank) and Bonus Cars (4 rows, Toy # blank) | Extracted + QA |
| 2000 | Present | 249 rows across 17 tables; 245 distinct nonblank Toy #; Virtual Collection and Bonus Cars require separate identifier scopes; five numeric Collector # values absent | Extracted + QA |
| 2001 | Present | Mainline: 240 rows, Collector # 001–240; separate Final Run: 12 rows; Store Exclusives: 4 rows with identifiers blank in source | Extracted + QA |
| 2002 | Present | Annual Mainline: 240 rows, Collector # 001–240; separate Final Run table: 3 rows with its own Series # namespace; 2002 Hot Wheels uses five-column schema | Extracted + QA |
| 2003 | Present | 222 rows across 22 tables; Collector # 001–220 continuous; one 5-column table omits Series #; #035 has three color rows | Extracted + QA |
| 2004 | Present | 268 rows across 16 tables; Collector # 001–212 continuous plus separate 000 Mail-In; four tables use five-column schema without Series # | Extracted + QA |
| 2005 | Present | 288 rows across 19 tables; Collector # 001–187 continuous; 2005 Open Stock (86 rows) has a five-column schema without Series # | Extracted + QA |
| 2006 | Present | 363 rows across 17 tables; Collector # 001–223 continuous; 2006 Open Stock has 141 rows in a distinct five-column schema without Series # | Extracted + QA |
| 2007 | Present | 315 rows across 18 tables, 180 numeric Collector # positions (001–180); 193 unique Toy #; all 315 Series # cells contain zero-width Unicode | Extracted + QA |
| 2008 | Present | 358 rows across 18 tables, 196 numeric Collector # positions (001–196); 208 unique Toy #, repeated across color variants | Extracted + QA |
| 2009 | Present | Mainline: 342 rows across 14 tables, 190 numeric Collector #; Toy # repeats among color entries; 12 Redline/Goodyear exclusive rows are exact repeats | Extracted + QA |
| 2010 USA | Present | Extracted + QA: 440 source rows across 28 tables, 252 unique Toy #, 240 Collector #; includes Goodyear/BF Goodrich sections | Extracted + QA; cross-page adjudication pending |
| 2010 International | Present | Extracted + QA: 228 source rows across 24 tables, 226 unique Toy #, 214 Collector # | Extracted + QA; cross-page adjudication pending |
| 2011 | Present | Mainline: 429 rows across 21 tables, numeric Collector # 001–244; 20 additional Windshield Banner/Redline exclusive rows are exact repeats of Mainline rows | Extracted + QA |
| 2012 | Present | Mainline: 387 rows across 23 tables, numeric Collector # 001–247; two cross-listed exclusives tables add 20 rows; Year of the Dragon Edition adds 1 No # row | Extracted + QA |
| 2013 | Present | Mainline: 433 rows across 30 series tables, 250 numeric Collector #; Scavenger Hunts: 6 rows in separate Kroger-exclusive table, Collector # = No #; Mainline schema has no Series # column | Extracted + QA |
| 2014 | Present | Mainline: 433 rows across 32 series tables, 250 numeric Collector #; Scavenger Hunt: 4 rows in separate Kroger-exclusive table; one Mainline table lacks Series # column | Extracted + QA |
| 2015 | Present | Mainline: 433 rows across 34 series tables, 250 numeric Collector #; Scavenger Hunt: 4 rows in separate 6-column table, Collector # = No #; Mainline schema has no Series # column | Extracted + QA |
| 2016 | Present | Mainline: 433 rows across 31 series tables, 250 numeric Collector #; 8 Special Edition rows in 2 additional tables, Collector # = No #; 397 Series # cells contain zero-width Unicode | Extracted + QA |
| 2017 | Present | Mainline #1–365: 365 rows; additional separately headed sections: 85 rows across 9 sections, all Collector # = No # | Extracted + QA |
| 2018 | Present | Mainline #1–365: 365 rows; additional separately headed sections: 104 rows across 10 assortments/exclusives/chase tables, all Collector # = No # | Extracted + QA |
| 2019 | Present | Mainline: 447 rows, 447 unique Toy #, 250 numeric Collector #; separate unnumbered Special Editions: 2 rows with Collector # = No # | Extracted + QA |
| 2020 | Present | Mainline: 447 rows, 447 unique Toy #, 250 numeric Collector #; separate Hot Wheels id Chase Series: 8 rows with Collector # = No #; 2 broken Photo filename placeholders | Extracted + QA |
| 2021 | Present | Mainline: 447 rows, 447 unique Toy #, 250 numeric Collector #; separate Hot Wheels id: Chase Series table: 8 rows with Collector # = No # | Extracted + QA |
| 2022 | Present | Full table extracted and QA checked: 447 rows, 447 unique Toy #, 250 Collector #, 142 rows marked (2nd Color), 15 TH + 15 STH | Extracted + QA |
| 2023 | Present | Full table extracted and QA checked: 445 rows, 445 unique Toy #, 250 Collector #, 141 rows marked (2nd Color), 15 TH + 15 STH | Extracted + QA |
| 2024 | Present | Full table re-extracted and QA checked: 441 rows, 441 unique Toy #, 250 Collector #, 132 rows marked (2nd Color), 15 TH + 15 STH; 49 prior Car Culture name-match candidates remain unadjudicated | Extracted + QA |
| 2025 | Present | Full extraction and QA documented: 440 rows, 440 unique Toy #, 250 Collector #, 146 rows marked (2nd Color); Premium comparisons completed | Extracted + QA |
| 2026 | Present | Full table extracted and QA checked: 440 rows, 440 unique Toy #, 250 Collector #, 137 rows marked (2nd Color), 15 TH + 15 STH | Extracted + QA |

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

1. Continue annual Mainline extraction and QA for 1968–1978. The 1997–2026 annual sources have been extracted/QA-checked; 2010 ordinary and International lists are separate, independently processed datasets.
2. Adjudicate the 2010 USA/International comparison: investigate 21 shared-Toy# model-name discrepancies, 13 International-only and 39 USA-only Toy # values, and the 18 USA tire-exclusive section rows.
3. Resolve year-specific anomalies already recorded for 1997–2009 (sparse Collector # ranges, repeated Toy #/Collector # values, separate program scopes, blank identifiers and schema differences).
4. Adjudicate the existing 49 Car Culture ↔ Mainline 2024 name-match candidates against the canonical 2024 extraction. Preserve the comparison as a separate run; name matches are not casting/tooling proof.
5. Adjudicate 2026 source notes and compare against adjacent annual lists; the 2026 annual table extraction and structural QA are complete.
6. Build year-scoped cross-program comparisons only after the relevant annual Mainline sources have verified extraction. Do not infer a match in another year from the 2024/2025 samples.

For every annual page, record source path, branch, Git blob SHA, manifest SHA-256, Fandom revision/date if available, extraction method/version, table boundaries, row counts, unique identifier counts, duplicate groups, and unresolved anomalies.

### 2010 dual-page extraction status

Both 2010 pages have been independently extracted and QA-checked. The exports preserve table index, section heading, row position, all six source columns, and the raw Collector-column header. The cross-page analysis is documented in `research/comparisons/MAINLINE-2010-USA-INTERNATIONAL.md`. Shared Toy # values are candidates only; Collector # values differ between the page scopes and must not be merged.

## 4. Data-model and QA cautions

- Mainline Toy # and Collector # are different identifier namespaces. Collector # is not a unique release key: regular and STH rows may share it.
- Color variants can have distinct Toy # while sharing Collector #; preserve raw labels such as `(2nd Color)`.
- Keep annual list row identity separate from casting identity and from the physical release/product identity.
- Treat regional/international lists as separate source scopes until compared.
- Do not treat the annual page's row count as the number of unique castings.
- Keep source assertions and uncertainty explicit; exact name matches do not prove casting/tooling identity.

## 5. Archive-wide inventory checkpoint

The Fandom archive tree currently contains 530 HTML/HTM files and 2 CSV files. This audit does not yet assign a final processing status to every Fandom HTML page. That is the next inventory phase, after Mainline. The planned next scope is Early Collections, Early Special Series, Other Early Series, then the remaining modern categories. Folder taxonomy is an archival organization, not a verified product hierarchy.
