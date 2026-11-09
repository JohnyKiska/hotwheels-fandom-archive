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

No other width, blank-record, exact-duplicate, BOM, U+FFFD, header-label, or quote-balance issue was found in the inspected files. Repeated product identifiers and variant records are not deduplicated. Full audit of the remaining 559 CSV files and page-QA output-path reconciliation are still outstanding.

## Fourth-stage progress update (2026-11-09)

Sequential CSV validation has now reached **122 of 633 distinct CSV files**. The additional Larger Scale and Mainline files inspected in this stage showed no malformed quoting, row-width mismatches, blank data records, exact duplicate rows, BOM, U+FFFD, or empty/duplicate header labels. The 19-column Mainline exports continue to validate against their own 19-column headers.

Header-only exports are not automatically defects: the two Exclusives files with zero data rows were matched to their page-level QA reports, which confirm zero product tables/rows and intentional header-only CSV output. Other header-only outputs will be reconciled against their QA reports during the output-path audit.
