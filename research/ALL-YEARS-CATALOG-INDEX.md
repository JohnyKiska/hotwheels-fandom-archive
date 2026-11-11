# All-years Catalog Index

The generated catalog index is the first usable cross-year data layer for the HW Catalog.

## Included scope
- Mainline: all available `MAINLINE-*.csv` extraction files, currently 1968–2026 with separate USA/International 2010 sources.
- Premium: extracted Car Culture, Car Culture 2-Pack, Team Transport, Boulevard, Fast & Furious Premium, Pop Culture and Entertainment family tables.
- The source inventory records each file and its row count. Source CSVs remain unchanged.

## Identity rules
- Mainline grouping uses year + Collector # when available. Earlier records without Collector # use year + normalized model name.
- Premium grouping uses year + family + source series + normalized model name.
- Groups with multiple source records are only `provisional_same_casting`. They are navigation and review candidates, not proof that the physical tooling is identical.
- No cross-year casting merge is made solely from matching model names.
- Explicit source notes such as "Identical to ..." and base-code references are retained as evidence leads.
- Mainline `Series` values are normalized: the actual series name is separated from trailing release labels such as `New for YYYY!`, `New in Mainline`, `Treasure Hunt`, `Super Treasure Hunt`, `Red Edition` and supported retailer exclusives. The original combined value is retained as `series_raw`; extracted labels are stored in `release_tags`, `release_type` and `exclusive`.
- Color, tampo, wheel type, finish and packaging remain variant attributes and do not independently create new casting identities.

## Outputs
- `catalog/generated/catalog-index.json`: source inventory, candidate groups and normalized records.
- `catalog/generated/catalog-index-stats.json`: compact counts for the UI.
- `scripts/build_catalog_index.py`: reproducible generator.
- `.github/workflows/build-catalog-index.yml`: rebuilds the index when source extraction CSVs change.

This is a read-only catalog index. It does not overwrite source extractions, the review queue, canonical database entities, or personal collection data.
