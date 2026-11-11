# Casting identity automation

## Default decision rule

The project now uses a **same-casting-until-difference-is-found** working assumption.

- Entries sharing a catalog grouping key are provisionally grouped as one casting.
- A new color, tampo, wheel style, finish, Treasure Hunt status, Super Treasure Hunt status, retailer exclusive, or packaging variation does not by itself establish a new casting.
- A group is split only when evidence points to a structural difference in the physical casting: body/tooling geometry, base construction, molded features, part layout, or other persistent physical construction.
- User physical inspection can promote a provisional group to `user_confirmed_same_casting`.
- Catalog names, Collector numbers, images, and automated similarity scores are evidence leads, not physical proof.
- Source rows, releases, variants, packaging, and assortments remain separate. Grouping castings never merges those records.

## Current Mainline 2026 MVP

Input: `research/reviews/MAINLINE-2026-VISUAL-REVIEW-QUEUE.csv`

Generator: `scripts/build_casting_review_groups.py`

Output: `research/reviews/MAINLINE-2026-PROVISIONAL-CASTING-GROUPS.csv`

The generator groups rows by Collector #, assigns a provisional or user-confirmed casting status, and flags naming/series conflicts, special releases, distribution variants, and available photo evidence. It does not modify the source queue or create canonical database entities.

GitHub Actions rebuilds the register whenever the review queue or generator changes. The output is a triage register, not an authoritative list of physically proven castings.

## Evidence and exception workflow

1. The generator groups records by the available catalog key.
2. Automated checks flag potential anomalies and collect source photo references.
3. Review focuses on exceptions, not on proving every color variant identical.
4. A structural difference creates a separate provisional casting candidate and an evidence note.
5. A user physical inspection can confirm or reject the split.
6. The decision is propagated to the canonical database only with provenance and an explicit status.

## Expansion plan

### Mainline across all years
- Inventory every extraction CSV and identify its native grouping key (Collector #, Toy #, series item, or another source-specific identifier).
- Generate one normalized candidate register while preserving source rows and source terminology.
- Use stable casting IDs only after the grouping key and evidence model are validated for that source family.
- Prioritize groups with conflicting model names, base/tooling references, structural image differences, or known casting revisions.

### Premium and other lines
- Keep separate source adapters for Premium, RLC, Monster Trucks, larger scales, Pro Racing, multipacks, and other families.
- Do not reuse Mainline Collector # assumptions across product families.
- Model scale, chassis/base, body shell, interior, wheel assemblies, moving parts, and package/set membership independently where the source supports them.
- Treat Premium series and packaging as release/assortment context, not automatically as casting identity.

## What automation can and cannot decide

Automation can reliably inventory records, normalize labels, group likely variants, find duplicate source entries, collect image evidence, and rank suspicious groups for review.

Image similarity can help find candidate differences, but different camera angles, lighting, paint, tampo, reflections, and wheel swaps create false positives. Similar photos also cannot prove identical hidden undersides or internal tooling. Final casting identity remains evidence-based and must distinguish automated hypotheses from physical confirmation.

## Success metric

The goal is to reduce manual work from checking every variant pair to reviewing only groups with meaningful structural or provenance conflicts, while keeping uncertainty visible and never silently turning a hypothesis into a fact.
