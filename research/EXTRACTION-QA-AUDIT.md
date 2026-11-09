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
