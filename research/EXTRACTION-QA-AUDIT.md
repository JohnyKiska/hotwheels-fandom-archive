# Extraction QA Audit

## Scope and status

This is a staged quality audit of the extracted CSV outputs in `research/extractions/`. It is separate from the page-coverage audit: 530/530 source HTML/HTM pages have individual extraction QA, and the directory currently contains 633 CSV files plus 530 page-level QA reports.

**Status: first-pass stratified spot-check in progress. This is not yet a full validation of all 633 CSV files.**

## Checks performed in the first pass

- Inspected 19 CSV outputs sampled across Early Collections, Early Special Series, Mainline, Exclusives, Miscellaneous, Modern Special Series, Notable Modern Themed Assortments, Other Modern Series, and Larger Scale.
- Checked header/data-row field counts using CSV-aware parsing, and scanned sampled files for Unicode replacement characters.
- The checked files showed consistent row widths after the correction below; no replacement characters were found in the sampled files.
- Sampled outputs include both the 21-column source-preserving extraction format and older section-specific schemas with different, intentional column counts. A single universal column count is therefore not a valid archive-wide rule.
- Duplicate values and repeated Toy # values must not be treated as errors by themselves. The extraction is source-preserving and intentionally retains repeated source rows and variant entries.

## Correction made

In `EARLY-COLLECTIONS-FLYING-COLORS.csv`, the separate `section_reference` row for Track Sets / Thundershift 500 had one surplus empty field and therefore 23 fields against the 22-column header. The surplus empty field was removed. The row now has 22 fields, with its reference metadata in the final `Raw source cells` column.

The matching QA report was updated to record the ancillary row and the schema-width correction.

## Next audit stages

1. Continue stratified CSV width and encoding checks across the remaining extraction families.
2. Verify each page-level QA report's declared output paths against the committed CSV inventory, including split outputs.
3. Review blank rows, exact duplicate rows, and suspicious repeated records without deleting source-preserved variants.
4. Record exceptions and fixes with source provenance; do not normalize or deduplicate product data during this structural QA pass.

## First-pass limitation

The 19-file sample is useful for catching obvious serialization defects but cannot establish that every CSV is structurally valid. Archive-wide validation remains open.


## Second-pass stratified spot-check (2026-11-09)

Nine additional CSV exports were parsed with CSV-aware quote handling, sampled across Early Special Series, Other Early Series, Mainline, Exclusives, Miscellaneous, Modern Special Series, Notable Modern Themed Assortments, Other Modern Series, and Larger Scale.

| CSV | Data rows | Columns | Width errors | Blank rows | Exact duplicate rows | U+FFFD |
|---|---:|---:|---:|---:|---:|---:|
| EARLY-SPECIAL-SERIES-ACTION-PACKS.csv | 32 | 21 | 0 | 0 | 0 | No |
| OTHER-EARLY-SERIES-ACTION-CYCLES.csv | 26 | 21 | 0 | 0 | 0 | No |
| MAINLINE-1968.csv | 42 | 19 | 0 | 0 | 0 | No |
| EXCLUSIVES-ELITE-64-PRODUCT-TABLES.csv | 38 | 21 | 0 | 0 | 0 | No |
| MISCELLANEOUS-1985-5-PACKS-PRODUCT-TABLES.csv | 1 | 21 | 0 | 0 | 0 | No |
| MODERN-SPECIAL-SERIES-100-PERCENT-HOT-WHEELS-1-43-SCALE.csv | 13 | 21 | 0 | 0 | 0 | No |
| NOTABLE-MODERN-THEMED-ASSORTMENTS-50TH-ANNIVERSARY-BLACK-AND-GOLD-SERIES-2018.csv | 7 | 21 | 0 | 0 | 0 | No |
| OTHER-MODERN-SERIES-2000-MONSTER-JAM-SERIES.csv | 4 | 21 | 0 | 0 | 0 | No |
| LARGER-SCALE-1-43-BATTLE-VEHICLES.csv | 13 | 21 | 0 | 0 | 0 | No |

All nine files had consistent record widths, no fully blank data rows, no exact duplicate data rows in this sample, no Unicode replacement characters, and balanced CSV quoting. The 19-column Mainline schema is intentional and confirms that archive-wide checks must compare each row with its own header rather than enforce one global width.

The repository tree contains same-stem QA reports for seven of the nine CSVs. No same-stem report was found for the Exclusives Elite 64 and Miscellaneous 1985 5-Packs split exports; these require mapping back to their source-page QA reports before treating the absence as an issue. This spot-check does not establish archive-wide validity.

## Third-stage CSV structural audit (2026-11-09)

The audit has expanded from stratified sampling to sequential file-by-file validation. A total of **74 distinct CSV files out of 633** have now been inspected; this remains an in-progress audit, not a completion claim.

Checks applied to the inspected files:
- CSV-aware parsing with quoted fields, escaped double quotes, and embedded line breaks.
- Each data record's field count compared with its own file's header (no archive-wide fixed schema).
- Empty data records, exact duplicate records, BOM, Unicode replacement character U+FFFD, empty/duplicate header labels, and malformed quote handling.

Two structural defects have been corrected during the expanded pass:
1. `EARLY-COLLECTIONS-FLYING-COLORS.csv`: one ancillary `section_reference` row had a surplus empty field (23 fields vs. 22-column header); removed the surplus empty field and updated its QA report.
2. `EARLY-COLLECTIONS-30TH-ANNIVERSARY-4-CAR-SET.csv`: each of the four product rows had one surplus empty field before `Photo filename`, shifting photo and provenance columns. Removed only that empty field; all four rows now match the 20-column header. The associated QA report documents the correction and preserves a note about two lazy-load image placeholders whose actual `data-src` URLs remain in raw source HTML.

No other width, blank-record, exact-duplicate, BOM, U+FFFD, header-label, or quote-balance issue was found in the inspected files. Repeated product identifiers and variant records are not deduplicated. Full audit of the remaining CSV files and page-QA output-path reconciliation are still outstanding.

## Fourth-stage progress update (2026-11-09)

Sequential CSV validation has now reached **122 of 633 distinct CSV files**. The additional Larger Scale and Mainline files inspected in this stage showed no malformed quoting, row-width mismatches, blank data records, exact duplicate rows, BOM, U+FFFD, or empty/duplicate header labels. The 19-column Mainline exports continue to validate against their own 19-column headers.

Header-only exports are not automatically defects: the two Exclusives files with zero data rows were matched to their page-level QA reports, which confirm zero product tables/rows and intentional header-only CSV output. Other header-only outputs will be reconciled against their QA reports during the output-path audit.

## Fifth-stage progress update (2026-11-09)

Sequential validation has advanced to **130 of 633 distinct CSV files**. The latest eight Mainline exports (1972–1979) all passed CSV parsing and per-file schema-width checks; no blank data records, exact duplicate rows, malformed quoting, BOM, U+FFFD, or empty/duplicate header labels were found. The 19-column schema remains internally consistent for these years.


## Sixth-stage progress update (2026-11-09)

Sequential CSV validation has advanced to **140 of 633 distinct CSV files**. Mainline years 1980–1989 all passed CSV parsing and per-file row-width checks, with no blank data records, exact duplicate rows, malformed quoting, BOM, U+FFFD, or empty/duplicate header labels. Mainline schema widths legitimately vary by period (19, 18, 17, and 9 columns in this batch); validation is therefore always performed against each individual file's own header, not a fixed global width. The narrower 1989 schema is recorded for later semantic/provenance reconciliation rather than treated as a defect based on width alone.

## Seventh-stage progress update (2026-11-09)

Sequential validation has advanced to **160 of 633 distinct CSV files**. Mainline 1990–1999 (10 files) and 2000–2009 (10 files) passed CSV parsing and row-width validation against each file's own header. No blank data records, exact duplicate rows, malformed quoting, BOM, U+FFFD, or empty/duplicate header labels were detected in these 20 files. Schema widths continue to evolve across the Mainline archive, with 25, 16, 13, 12, 11, and 10-column layouts represented; these differences are retained and not treated as errors without evidence of a row/header mismatch or lost source fields.


## Machine-readable audit manifest and next Mainline batch (2026-11-09)

Added `research/CSV-AUDIT-MANIFEST.csv` with one row for each of the 633 CSV exports. It records per-file audit status and structural-check fields. Because the earlier aggregate progress counters (including 160/633) were not backed by a durable per-file manifest, those historical checks are deliberately left as `not_yet_audited` in the new manifest rather than guessed or reconstructed from a count alone. This is a conservative tracking baseline, not a claim that those files were never inspected.

The following ten Mainline exports were newly validated and recorded as `checked` in the manifest:

| CSV | Data rows | Columns | Width errors | Blank rows | Exact duplicate extra rows |
|---|---:|---:|---:|---:|---:|
| MAINLINE-2011.csv | 449 | 10 | 0 | 0 | 0 |
| MAINLINE-2012.csv | 408 | 10 | 0 | 0 | 0 |
| MAINLINE-2013.csv | 439 | 11 | 0 | 0 | 0 |
| MAINLINE-2014.csv | 437 | 11 | 0 | 0 | 0 |
| MAINLINE-2015.csv | 437 | 11 | 0 | 0 | 0 |
| MAINLINE-2016.csv | 441 | 10 | 0 | 0 | 0 |
| MAINLINE-2017.csv | 450 | 10 | 0 | 0 | 0 |
| MAINLINE-2018.csv | 469 | 10 | 0 | 0 | 0 |
| MAINLINE-2019.csv | 449 | 10 | 0 | 0 | 0 |
| MAINLINE-2020.csv | 455 | 10 | 0 | 0 | 0 |

All ten files passed CSV-aware parsing, per-file row-width checks, blank-row checks, exact-duplicate-row checks, BOM, U+FFFD, empty/duplicate-header checks, and quote-balance validation. No structural defects were found. Repeated Toy # values or similar-looking source variants were not deduplicated.

Manifest creation commit: `81f9ecfa23434c42ad80f0db1186b67ab2292576`. Manifest provenance update commit: `47b23e9cd2b0e731d4062c6da79ee83019aa16c4`.


## Mainline final available years (2026-11-09)

Five further Mainline exports passed the same CSV-aware structural checks and were added to the machine-readable manifest:

| CSV | Data rows | Columns | Width errors | Blank rows | Exact duplicate extra rows |
|---|---:|---:|---:|---:|---:|
| MAINLINE-2021.csv | 455 | 10 | 0 | 0 | 0 |
| MAINLINE-2022.csv | 447 | 6 | 0 | 0 | 0 |
| MAINLINE-2023.csv | 445 | 6 | 0 | 0 | 0 |
| MAINLINE-2024.csv | 441 | 6 | 0 | 0 | 0 |
| MAINLINE-2026.csv | 440 | 6 | 0 | 0 | 0 |

All five files had balanced quoting, no BOM/U+FFFD, no blank rows, no exact duplicate rows, and no empty or duplicate header labels. The schema change from 10 to 6 columns is retained as represented by each file's own header; it is not treated as a defect. The repository contains no `MAINLINE-2025.csv`, so no file for that year was assumed or created. Manifest update commit: `96500c84c5b10190caae4e06ef6683ac59c033c8`.


## CSV-to-QA filename reconciliation (2026-11-09)

A repository-tree reconciliation found 633 CSV exports, 530 page-level extraction QA reports under `research/extractions/`, and 63 additional QA reports under `research/qa/` (593 QA documents total). The audit manifest now includes `qa_report_path` and `qa_reconciliation_status` for every CSV.

- 632 of 633 CSVs map to a QA report by the repository's filename conventions, including split exports mapped to their parent page report and product-table exports mapped to the corresponding report under `research/qa/`.
- One CSV remains without a standalone QA report: `research/extractions/MAINLINE-2010-USA.csv`. The repository contains `MAINLINE-2010-INTERNATIONAL-EXTRACTION-QA.md` and a comparison note at `research/comparisons/MAINLINE-2010-USA-INTERNATIONAL.md`, but no dedicated USA extraction QA report. Treat this as an unresolved documentation gap, not as evidence that the CSV itself is invalid.
- The six modern-series reports with non-matching report/export stems were inspected and their split CSV parts were confirmed from the QA text: Color Reveal (2 parts), Hot Wheels Classics (6), List of 2010 Hot Wheels (2), List of 2013 Hot Wheels (2), List of 2014 Hot Wheels (2), and Mario Kart (2).
- Sampled direct-output and legacy `research/qa/` reports confirm the established filename mapping pattern. The manifest deliberately labels the broader mapping `matched_by_filename_convention`; it does not overstate every mapping as an individually inspected explicit output declaration.

Manifest reconciliation commit: `0ebeb79cdf691277efd687de34cfc30123376b90`.

This is a filename-level reconciliation milestone, not completion of the full CSV structural audit or the entire 530-report content review. The unresolved USA QA gap and full declared-output review remain open. Gallery extraction remains blocked until all 633 CSVs have passed the full audit and the QA/output-path reconciliation is closed.


## Early Collections structural audit batch (2026-11-09)

Ten Early Collections CSV exports were re-fetched and parsed with CSV-aware quoting rules. Each file was checked against its own header width; no cross-file/global schema was imposed.

| CSV | Data rows | Header columns | Width errors | Blank rows | Exact duplicate extra rows |
|---|---:|---:|---:|---:|---:|
| EARLY-COLLECTIONS-30TH-ANNIVERSARY-4-CAR-SET.csv | 4 | 20 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-ACTION-COMMAND.csv | 38 | 16 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-BOSS-HOSS.csv | 55 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-CLASSICS.csv | 25 | 18 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-CLASSY-CUSTOMS.csv | 14 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-DRAG-STRIPPERS.csv | 19 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-EVIL-WEEVIL.csv | 37 | 23 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-EXTRAS.csv | 9 | 23 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-FLYING-COLORS.csv | 213 | 22 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-GRAND-PRIX.csv | 12 | 26 | 0 | 0 | 0 |

All ten also passed balanced-quote, BOM, U+FFFD, empty-header and duplicate-header checks. No exact duplicate data rows were found. Source rows and repeated Toy # values were not deduplicated or otherwise altered. The manifest records these ten files as checked. Manifest update commit: `f78593385de3eb7c1660271e3bc4e626b347d8a7`.


## Early Collections structural audit batch 2 (2026-11-09)

Ten further Early Collections CSV exports were parsed with CSV-aware quote handling and checked against their individual headers.

| CSV | Data rows | Header columns | Width errors | Blank rows | Exact duplicate extra rows |
|---|---:|---:|---:|---:|---:|
| EARLY-COLLECTIONS-HEAVY-CHEVY.csv | 77 | 23 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-HEAVYWEIGHTS.csv | 13 | 11 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-HIRAKERS.csv | 18 | 17 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-KING-KUDA.csv | 99 | 17 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-LIGHT-MY-FIREBIRD.csv | 33 | 17 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-MEGAFORCE-SERIES.csv | 7 | 9 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-NITTY-GRITTY-KITTY.csv | 42 | 14 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-OLDIES-BUT-GOODIES.csv | 10 | 14 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-REAL-RIDERS.csv | 31 | 8 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-RESCUE-TEAM.csv | 8 | 14 | 0 | 0 | 0 |

All ten files passed malformed-quote, BOM, U+FFFD, empty-header and duplicate-header checks. No blank data rows, exact duplicate data rows, or row-width mismatches were found. Different header widths are intentional and validated per file. No source rows were removed or normalized.

Manifest update commit: `df1a9d2191d75ec77590384c4559d1de81dca859`.


## Early Collections structural audit batch 3 (2026-11-09)

Ten further Early Collections CSV exports were parsed with CSV-aware quote handling and checked against their individual headers.

| CSV | Data rows | Header columns | Width errors | Blank rows | Exact duplicate extra rows |
|---|---:|---:|---:|---:|---:|
| EARLY-COLLECTIONS-SPEED-DEMONS.csv | 22 | 14 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-SPEED-FLEET.csv | 76 | 17 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-SPEED-MACHINES-1983.csv | 28 | 14 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-SPEEDWAY-SPECIALS.csv | 19 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-SUGAR-CADDY.csv | 20 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-SUPER-CHROMES-1976.csv | 50 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-SUPER-STREETERS.csv | 21 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-THE-HEAVIES.csv | 9 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-THE-HOT-ONES-1981.csv | 117 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-TNT-BIRD.csv | 22 | 21 | 0 | 0 | 0 |

All ten files passed malformed-quote, BOM, U+FFFD, empty-header and duplicate-header checks. No blank data rows, exact duplicate data rows, or row-width mismatches were found. Different header widths are intentional and validated per file. No source rows were removed or normalized.

Manifest update commit: `d8b37f5d3d9f7f3aa53bca5790e75f68a0c4ce4b`.


## Early Collections and Early Special Series structural audit batch 4 (2026-11-09)

Twenty CSV exports were fetched from `main` and parsed with CSV-aware quoting rules. Every data row was checked against its own file's header; no global schema was imposed. The audit also checked physical blank/whitespace-only lines (excluding a final newline), exact duplicate full rows, malformed quoting, BOM, U+FFFD, empty/duplicate headers, and trailing delimiters.

| CSV | Data rows | Header columns | Width errors | Blank rows | Exact duplicate extra rows |
|---|---:|---:|---:|---:|---:|
| EARLY-COLLECTIONS-TRAILBUSTERS.csv | 49 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-ULTRA-HOTS-SERIES-1984.csv | 26 | 21 | 0 | 0 | 0 |
| EARLY-COLLECTIONS-WORKHORSES.csv | 86 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-ACTION-PACKS.csv | 32 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-AUTO-CITY.csv | 87 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-CALIFORNIA-CUSTOM-SERIES.csv | 57 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-CHOPCYCLES.csv | 9 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-COLOR-CHANGERS.csv | 133 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-COLOR-FX.csv | 34 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-CONVERTABLES.csv | 13 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-CRACK-UPS.csv | 43 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-CRASHERS-1999.csv | 17 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-CRASHERS-2007.csv | 53 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-FARBS.csv | 4 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-FIREWORKS.csv | 4 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-FLIP-OUTS.csv | 9 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-FLIPPERS.csv | 37 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-GRAN-TOROS.csv | 29 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-HIWAY-HAULER.csv | 4 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-HOT-BIRDS.csv | 15 | 21 | 0 | 0 | 0 |

All twenty passed: no row-width errors, blank/whitespace-only rows, exact duplicate full rows, malformed quotes, BOM, U+FFFD, empty or duplicate headers, or trailing delimiters. Source data was not normalized, deduplicated, or modified. Repeated values within fields were retained.

Total data rows inspected in this batch: **741**. Manifest update commit: `810f88c58499e9fbeb85d8a7a78d6ba70bcbf31b`. The manifest records the pre-update branch HEAD as checked provenance: `25bb51821e02bbb4217bef75e081687adab1aff4`.


## Early Special Series structural audit batch 5 (2026-11-09)

Twenty further Early Special Series CSV exports were re-fetched from `main` and parsed with CSV-aware quoting rules. Every data row was checked against its own file's header; no global schema was imposed. Checks covered physical blank/whitespace-only lines (excluding a final newline), exact duplicate full rows, malformed quoting, BOM, U+FFFD, empty/duplicate headers, and trailing delimiters. The corresponding QA report was fetched for each CSV, and each report's declared product-row count matched the parsed CSV data-row count.

| CSV | Data rows | Header columns | Width errors | Blank rows | Exact duplicate extra rows |
|---|---:|---:|---:|---:|---:|
| EARLY-SPECIAL-SERIES-HOT-LINE.csv | 20 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-HOT-SHOTS.csv | 8 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-HOT-WHEELS-U-S-A.csv | 14 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-HOT-WHEELS-WORLD.csv | 117 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-LAW-MILL.csv | 2 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-MOTORIZED-X-V-RACERS.csv | 101 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-NEEDLE-NOSE.csv | 5 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-PLANET-MICRO.csv | 197 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-RAM-ROCKET.csv | 4 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-RED-BARON-SIZZLERS.csv | 1 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-REVVERS.csv | 41 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-RRRUMBLERS.csv | 60 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-SCORCHERS.csv | 24 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-SHIFT-KICKERS.csv | 6 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-SIZZLERS.csv | 65 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-SMALL-SHOTS.csv | 14 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-STEERING-RIGS.csv | 34 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-STEERING-TRAILER.csv | 1 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-SUPER-CALIFORNIA-CUSTOM.csv | 12 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-TRUCK-CO.csv | 20 | 21 | 0 | 0 | 0 |

All twenty passed: no row-width errors, blank/whitespace-only rows, exact duplicate full rows, malformed quotes, BOM, U+FFFD, empty or duplicate headers, or trailing delimiters. All twenty QA report row counts matched the CSVs and the manifest filename mapping was confirmed. Source data was not normalized, deduplicated, or modified. Repeated values within fields were retained.

Total data rows inspected in this batch: **746**. Manifest update commit: `9db8ae40c022d91669280cc82e32cc7deb0baa3c`. The manifest records the pre-update branch HEAD as checked provenance: `30d7afeb7166099545897ff04ec25b410964d049`.


## CSV structural audit batch 6 (2026-11-09)

Twenty CSV exports across Early Special Series, Exclusives and Larger Scale were re-fetched from `main` and parsed with CSV-aware quoting rules. Every data row was checked against its own file header. Checks covered row-width consistency, physical blank/whitespace-only lines, exact duplicate full rows, malformed quoting, BOM, U+FFFD, empty/duplicate headers and trailing delimiters. All twenty corresponding QA reports were fetched; each declared product-row count matched the parsed CSV count.

| CSV | Data rows | Columns | Width errors | Blank rows | Exact duplicate extra rows |
|---|---:|---:|---:|---:|---:|
| EARLY-SPECIAL-SERIES-X-V-RACERS.csv | 10 | 21 | 0 | 0 | 0 |
| EARLY-SPECIAL-SERIES-ZOWEES.csv | 14 | 21 | 0 | 0 | 0 |
| EXCLUSIVES-ELITE-64-PRODUCT-TABLES.csv | 38 | 21 | 0 | 0 | 0 |
| EXCLUSIVES-HOTWHEELSCOLLECTORS-COM-PRODUCT-TABLES.csv | 0 | 21 | 0 | 0 | 0 |
| EXCLUSIVES-RED-LINE-CLUB-PRODUCT-TABLES.csv | 0 | 21 | 0 | 0 | 0 |
| EXCLUSIVES-VIRTUAL-GARAGE-PRODUCT-TABLES.csv | 702 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-1-43-BATTLE-VEHICLES.csv | 13 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-1-43-PULL-BACKS.csv | 23 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-1-43-TURBOS-COLLECTION.csv | 8 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-100-HOT-WHEELS-1-18-SCALE.csv | 125 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-BATMAN-1-50-SCALE-SERIES.csv | 115 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-FERRARI-1-18-SCALE-SERIES.csv | 27 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-FERRARI-1-24-SCALE-SERIES.csv | 9 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-FERRARI-1-43-SCALE-SERIES.csv | 23 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-FORMULA-FUELERS.csv | 26 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-1-18-SCALE-SERIES.csv | 160 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-1-24-SCALE-SERIES.csv | 1 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-CLASSICS-1-18-SCALE.csv | 31 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-COLLECTIBLES-1-18-SCALE.csv | 23 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-ELITE-1-18-SCALE.csv | 208 | 21 | 0 | 0 | 0 |

All twenty passed the structural checks. Two header-only Exclusives exports were reconciled to their source-specific QA reports: HotWheelsCollectors.com has zero HTML table elements; Red Line Club has three navigation/ancillary tables without column headers. Both QA reports explicitly state zero product tables/rows and a 21-column header-only CSV, so these are expected zero-row outputs rather than unexplained extraction failures. The CSV files were not normalized or modified; source values and repetitions were preserved.

Total data rows inspected in this batch: **1,556**. Manifest provenance records the branch HEAD before this audit update: `215d4df235761241f23f30515add44f4e77af244`.

## CSV structural audit batch 7 (2026-11-09)

Twenty further Larger Scale CSV exports were re-fetched from `main` and parsed with CSV-aware quoting rules. Every data row was checked against its own file header. Checks covered row-width consistency, physical blank/whitespace-only lines, exact duplicate full rows, malformed quoting, BOM, U+FFFD, empty/duplicate headers and trailing delimiters. All twenty corresponding QA reports were fetched; each declared product-row count matched the parsed CSV count.

| CSV | Data rows | Columns | Width errors | Blank rows | Exact duplicate extra rows |
|---|---:|---:|---:|---:|---:|
| LARGER-SCALE-HOT-WHEELS-ELITE-1-43-SCALE.csv | 177 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-ELITE-ONE.csv | 6 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-LETS-RACE-ACTIVATE.csv | 9 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-RACING-1-18-SCALE.csv | 138 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-RACING-1-24-SCALE.csv | 23 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-RACING-1-43-SCALE.csv | 57 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-RACING-SERIES-2005.csv | 6 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-RACING-SERIES-2007.csv | 4 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-RACING-SERIES-2009.csv | 16 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HOT-WHEELS-XL.csv | 39 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HW-RACING-SERIES-2010.csv | 22 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HW-RACING-SERIES-2011.csv | 22 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-HW-RACING-SERIES-2012.csv | 22 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-LA-STORIA.csv | 5 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-PASSIONE.csv | 7 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-PREMIUM-1-43.csv | 41 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-PRO-RACING-1-43-SCALE.csv | 41 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-PULL-BACK-SPEEDERS.csv | 0 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-PULLBAX.csv | 23 | 21 | 0 | 0 | 0 |
| LARGER-SCALE-RACING-CIRCUIT-SERIES-2017.csv | 10 | 21 | 0 | 0 | 0 |

All twenty passed the structural checks. No row-width errors, blank/whitespace-only rows, exact duplicate full rows, malformed quotes, BOM, U+FFFD, empty or duplicate headers, or trailing delimiters were found. All twenty QA report product-row counts matched the CSVs. The header-only `LARGER-SCALE-PULL-BACK-SPEEDERS.csv` was reconciled against its QA report: the source HTML has no qualifying product table (no Toy # plus casting/model/name headers); one non-product table was excluded. This is an expected zero-row export, not an unexplained extraction failure. CSV source values were not normalized, deduplicated, or modified.

Total data rows inspected in this batch: **668**. Manifest update commit: `200eaaefb0a0fb9de2f17557fca706f77eddc56a`. The manifest records the branch HEAD before this audit update: `31b0fbcf37761a3af800930e6294c69b8cdcc80d`.

## CSV structural audit batch 8 (2026-11-09)

Twenty CSV exports spanning the final Larger Scale files and Mainline 1968–1984 were fetched from `main` and parsed with CSV-aware quoting rules. Every record was checked against its own header. Checks covered row-width consistency, physical blank/whitespace-only lines, exact duplicate full rows, malformed quoting, BOM, U+FFFD, empty/duplicate headers, and trailing delimiters. Each corresponding QA report was reviewed and its declared total CSV row count or gallery/product inventory count reconciled to the exported CSV row count.

| CSV | Data rows | Columns | Width errors | Blank rows | Duplicate extra rows | Trailing delimiters |
|---|---:|---:|---:|---:|---:|---:|
| LARGER-SCALE-STREET-POWER.csv | 163 | 21 | 0 | 0 | 0 | 0 |
| LARGER-SCALE-TEAM-HOT-WHEELS-RACING-SERIES-2008.csv | 4 | 21 | 0 | 0 | 0 | 0 |
| LARGER-SCALE-TUNERZ.csv | 21 | 21 | 0 | 0 | 0 | 0 |
| MAINLINE-1968.csv | 42 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1969.csv | 25 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1970.csv | 37 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1971.csv | 39 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1972.csv | 7 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1973.csv | 34 | 19 | 0 | 0 | 0 | 34 |
| MAINLINE-1974.csv | 25 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1975.csv | 31 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1976.csv | 41 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1977.csv | 103 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1978.csv | 54 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1979.csv | 51 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1980.csv | 49 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1981.csv | 27 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1982.csv | 90 | 19 | 0 | 0 | 0 | 0 |
| MAINLINE-1983.csv | 67 | 18 | 0 | 0 | 0 | 0 |
| MAINLINE-1984.csv | 35 | 18 | 0 | 0 | 0 | 0 |

All twenty files have consistent row widths, no blank/whitespace-only rows, no exact duplicate full rows, no malformed quotes, no BOM, no U+FFFD, and no empty or duplicate headers. QA inventory counts reconcile across all twenty files. The 34 trailing delimiters in `MAINLINE-1973.csv` are intentional empty final fields in the exported raw-source metadata; each row still has exactly 19 fields matching its 19-column header. They are not malformed rows or width errors. The 1968–1973 exports include gallery inventory rows as specified by their QA reports; these rows are retained as source records and not reclassified as product-table castings. CSV source values were not normalized, deduplicated, or modified.

Total data rows inspected in this batch: **945**. Manifest update commit: `304a9f963e4300f7ac95b0786a51bbe1abc293bf`. The manifest records the branch HEAD before this audit update: `49a8e3a4b2cdd9cbd04d31dcd4a68e4ba83ed449`.

## CSV structural audit batch 9 (2026-11-09)

Twenty Mainline CSV exports for 1985–2004 were fetched from `main`, parsed with CSV-aware quoting rules, and checked against their individual headers. The corresponding QA report for every export was fetched using the exact `qa_report_path` in the manifest. QA source-row totals reconcile with all 20 CSV data-row counts, including multi-table and multi-scope years; the CSV row total is not reduced to annual numbered-list counts where the export also retains separate source scopes.

| CSV | Data rows | Columns | Width errors | Blank rows | Exact duplicate extra rows |
|---|---:|---:|---:|---:|---:|
| MAINLINE-1985.csv | 38 | 18 | 0 | 0 | 0 |
| MAINLINE-1986.csv | 26 | 18 | 0 | 0 | 0 |
| MAINLINE-1987.csv | 23 | 17 | 0 | 0 | 0 |
| MAINLINE-1988.csv | 27 | 17 | 0 | 0 | 0 |
| MAINLINE-1989.csv | 76 | 9 | 0 | 0 | 0 |
| MAINLINE-1990.csv | 87 | 18 | 0 | 0 | 0 |
| MAINLINE-1991.csv | 62 | 18 | 0 | 0 | 0 |
| MAINLINE-1992.csv | 24 | 18 | 0 | 0 | 0 |
| MAINLINE-1993.csv | 72 | 25 | 0 | 0 | 0 |
| MAINLINE-1994.csv | 14 | 16 | 0 | 0 | 0 |
| MAINLINE-1995.csv | 97 | 13 | 0 | 0 | 0 |
| MAINLINE-1996.csv | 141 | 11 | 0 | 0 | 0 |
| MAINLINE-1997.csv | 151 | 12 | 0 | 0 | 0 |
| MAINLINE-1998.csv | 189 | 13 | 0 | 0 | 0 |
| MAINLINE-1999.csv | 212 | 11 | 0 | 0 | 0 |
| MAINLINE-2000.csv | 249 | 11 | 0 | 0 | 0 |
| MAINLINE-2001.csv | 256 | 11 | 0 | 0 | 0 |
| MAINLINE-2002.csv | 243 | 10 | 0 | 0 | 0 |
| MAINLINE-2003.csv | 222 | 11 | 0 | 0 | 0 |
| MAINLINE-2004.csv | 268 | 11 | 0 | 0 | 0 |

All twenty files passed the structural checks: no row-width errors, physical blank/whitespace-only rows, exact duplicate full rows, malformed quotes, BOM, U+FFFD, empty headers, duplicate headers, or trailing delimiters. The differing column counts reflect the preserved source/export schemas, including the compact five-column annual tables in 1989 and later years, rather than structural defects. QA reconciliation was checked against each report's complete source-row scope: for example, 1997 retains the numbered list, Bonus Cars and other series (151 rows total); 1999 retains the annual list, Final Run and Bonus Cars (212 total); and 2004 retains all 16 product tables (268 total). CSV source values were not normalized, deduplicated, or modified.

Total data rows inspected in this batch: **2,477**. Manifest update commit: `c02a4d842ad6825a166983b8a9e3201bae692d5e`. The manifest records the branch HEAD before this audit update: `cc8df64c2668158a147c173d73cb3ddb568b0ef0`.
