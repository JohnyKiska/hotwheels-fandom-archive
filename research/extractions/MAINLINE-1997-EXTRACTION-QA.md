# Mainline 1997: extraction and QA

## Source provenance

- Repository: `JohnyKiska/hotwheels`
- Branch: `archive/historical-html-1968-2026`
- Path: `ALLHW/1997/List of 1997 Hot Wheels _ Hot Wheels Wiki _ Fandom.html`
- Git blob SHA: `26c70ee039eb20be9af615bdd92bf15265f51acc`
- File size: 514,850 bytes
- Fandom revision: 799665
- Manifest SHA-256: `aa220c4509151caa43c911720bf0cf892f195bb068b241d3db501559056f56e2`

Machine-readable export: [MAINLINE-1997.csv](MAINLINE-1997.csv). It preserves table index, section heading, row position, raw cell count, original column headers and all source values. The 1997 Hot Wheels table uses five columns without Series #.

## QA results

| Scope | Tables | Rows | Identifier behavior |
|---|---:|---:|---|
| Numbered 1997 list | 15 | 119 | 119 unique numeric Collector # values, 147–642 |
| Bonus Cars | 1 | 4 | Collector # 001–004, separate scope |
| Other series | 7 | 28 | Collector # = N/A |
| Total | 23 | 151 | Preserve three scopes |

Numbered-list checks:

- 119 rows, 119 unique numeric Collector # values, spanning 147–642.
- 118 unique Toy # values; Toy #11850 occurs twice in two numbered tables with the same Model Name but different Collector # (563 and 248).
- 377 numeric values between 147 and 642 are not represented in this page. This is a non-dense identifier range, not an automatic list of missing products.
- 12 Treasure Hunt rows.
- No `(2nd Color)` or Super Treasure Hunt rows identified.
- The 1997 Hot Wheels table has 47 rows and a five-column schema without Series #.

Bonus Cars:

- Four rows with Collector # 001–004. Keep separate from the numbered 1997 list.

Other series (28 rows):

- Ferrari Series
- Classics Series
- Racing Series
- Street Racers Series
- Construction Series
- Road Repair Series
- Cabriolet Series

All 28 rows use Collector # = `N/A`, not a numeric Mainline Collector #. Construction Series includes a source row labelled `Breakaway Bucket (Unreleased)`; preserve this status as a source assertion, not a confirmed production fact.

## Cross-table Toy # anomalies

- Toy #11850: Splittin' Image II appears in White Ice Series (#563) and 1997 Hot Wheels (#248), same model name but different Collector #.
- Toy #15789: Porsche 911 appears in 1997 Hot Wheels (#590) and Street Racers Series (Collector # N/A).
- Toy #18365: 1997 Hot Wheels identifies the Toy # as Pontiac Salsa (#596), while Classics Series identifies it as Auburn 852 (Collector # N/A). This is a high-priority source conflict; do not merge automatically.

## Interpretation notes

- Collector # range 147–642 is sparse; the 377 unrepresented numbers are coverage observations only.
- Scope numeric Collector # by source/program. Bonus Cars and N/A series are not part of the numbered annual list.
- The 1997 Hot Wheels table omits Series # by source design.
- Preserve the literal `N/A` Collector # values and the `Unreleased` label.
- The archived Fandom page does not independently verify Mattel release status or tooling identity.
