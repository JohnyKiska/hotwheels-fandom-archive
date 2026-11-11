#!/usr/bin/env python3
"""Build a read-only visual export from the validated Pro Racing 1:43 SQLite pilot."""
from __future__ import annotations

import csv
import html
import json
import re
import sqlite3
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "pro-racing-1-43-visual-export.sqlite"
SCHEMA = ROOT / "database" / "schema.sql"
SEEDS = [
    ROOT / "database" / "pilot" / "pro-racing-1-43-seed.sql",
    ROOT / "database" / "pilot" / "pro-racing-1-43-reconciliation-seed.sql",
    ROOT / "database" / "pilot" / "pro-racing-1-43-casting-candidates.sql",
]
PILOT = ROOT / "database" / "pilot"
ASSET_DIR = PILOT / "assets" / "pro-racing-1-43"
OUTPUT = PILOT / "pro-racing-1-43-visual-export.json"


class TextOnly(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def text(self, value: str) -> str:
        self.parts = []
        self.feed(value or "")
        return " ".join(" ".join(self.parts).split())


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def count(conn: sqlite3.Connection, sql: str) -> int:
    return int(conn.execute(sql).fetchone()[0])


def main() -> int:
    for path in [SCHEMA, *SEEDS]:
        if not path.is_file():
            raise SystemExit(f"Required database input missing: {path.relative_to(ROOT)}")

    variant_rows = {r["source_row_number"]: r for r in read_csv(PILOT / "PRO-RACING-1-43-VARIANT-CANDIDATES.csv")}
    release_rows = {r["source_row_number"]: r for r in read_csv(PILOT / "PRO-RACING-1-43-RELEASE-ASSORTMENT-CANDIDATES.csv")}
    image_reviews = {r["gallery_item_index"]: r for r in read_csv(PILOT / "pro-racing-1-43-image-review.csv")}
    group_reviews = {r["review_group_id"]: r for r in read_csv(PILOT / "PRO-RACING-1-43-MATCH-RECONCILIATION.csv")}

    assets: dict[int, str] = {}
    for asset in ASSET_DIR.glob("*.webp"):
        match = re.match(r"^(\d{3})_", asset.name)
        if match:
            assets[int(match.group(1))] = asset.name

    DB.unlink(missing_ok=True)
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        conn.executescript(SCHEMA.read_text(encoding="utf-8"))
        for seed in SEEDS:
            conn.executescript(seed.read_text(encoding="utf-8"))

        product_rows = conn.execute(
            """SELECT source_row_id, source_row_number, raw_headers_json, raw_cells_json
               FROM source_row
               WHERE source_document_id='doc-pr143-products'
               ORDER BY source_row_number"""
        ).fetchall()
        source_records = []
        for row in product_rows:
            # raw_cells_json preserves the original product-table column order.
            headers = ["Casting", "Year", "Color", "Tampo", "Base Color", "Interior Color", "Wheel Type", "Toy #", "Country", "Notes", "Photo"]
            raw_cells = json.loads(row["raw_cells_json"])
            cells = {}
            for index, header in enumerate(headers):
                cell = raw_cells[index] if index < len(raw_cells) else {}
                cells[header] = cell.get("text", "") if isinstance(cell, dict) else str(cell)
            n = str(row["source_row_number"])
            variant = variant_rows.get(n, {})
            release = release_rows.get(n, {})
            source_records.append({
                "id": f"source-{int(n):03d}",
                "sourceRowId": row["source_row_id"],
                "recordType": "source_row",
                "name": cells.get("Casting", "") or f"Source row {n}",
                "year": cells.get("Year", ""),
                "sourceRowNumber": int(n),
                "sourceSection": "Vehicles",
                "color": cells.get("Color", ""),
                "sticker": cells.get("Sticker", ""),
                "tampo": cells.get("Tampo", ""),
                "baseColorOrType": cells.get("Base Color", ""),
                "windowColor": cells.get("Window Color", ""),
                "interiorColor": cells.get("Interior Color", ""),
                "wheelType": cells.get("Wheel Type", ""),
                "toyNumber": cells.get("Toy #", ""),
                "country": cells.get("Country", ""),
                "sourceNotes": cells.get("Notes", ""),
                "sourcePhoto": cells.get("Photo", ""),
                "variantCandidateId": variant.get("variant_candidate_id", ""),
                "variantDisposition": variant.get("review_disposition", "hold"),
                "variantReviewRationale": variant.get("review_rationale", ""),
                "releaseDisposition": release.get("release_review_disposition", "hold_release_details"),
                "releaseCandidateId": release.get("release_candidate_id", ""),
                "assortmentCandidateId": release.get("assortment_candidate_id", ""),
                "releaseReviewRationale": release.get("review_rationale", ""),
                "verificationStatus": "source_assertion_only",
                "canonicalEntityCreated": False,
                "visualStatus": "requires_review",
            })

        image_rows = conn.execute(
            """SELECT image_id, file_name, image_url, file_page_url, image_alt,
                      image_title, caption_html, source_row_id
               FROM image_asset
               WHERE source_document_id='doc-pr143-gallery'
               ORDER BY image_id"""
        ).fetchall()
        gallery_evidence = []
        parser = TextOnly()
        for row in image_rows:
            match = re.search(r"(\d{3})$", row["image_id"])
            if not match:
                raise SystemExit(f"Cannot derive gallery index from {row['image_id']}")
            n = int(match.group(1))
            review = image_reviews.get(str(n), {})
            group_id = review.get("review_group_id", "")
            group = group_reviews.get(group_id, {})
            asset = assets.get(n)
            if not asset:
                raise SystemExit(f"Downloaded WebP asset missing for Gallery item {n}")
            caption = row["caption_html"] or review.get("source_caption_html", "")
            gallery_evidence.append({
                "id": f"gallery-{n:03d}",
                "recordType": "gallery_evidence",
                "galleryItemIndex": n,
                "reviewGroupId": group_id,
                "groupLabel": review.get("group_label", ""),
                "fileName": row["file_name"],
                "assetFile": asset,
                "imageUrl": f"https://raw.githubusercontent.com/JohnyKiska/hotwheels-fandom-archive/main/database/pilot/assets/pro-racing-1-43/{asset}",
                "sourceCaption": caption,
                "sourceCaptionText": parser.text(caption),
                "candidateEntity": review.get("candidate_entity", ""),
                "candidateRelationScope": review.get("candidate_relation_scope", ""),
                "textConfidence": review.get("text_confidence", "unresolved"),
                "evidenceBasis": review.get("evidence_basis", ""),
                "imageReviewStatus": review.get("review_status", ""),
                "visualInspectionStatus": review.get("visual_inspection_status", ""),
                "reviewNotes": review.get("review_notes", ""),
                "groupDecision": group.get("decision", "UNRESOLVED"),
                "groupConfidence": group.get("match_confidence", "unresolved"),
                "visualStatus": "image_inspected_identity_not_necessarily_verified",
                "canonicalRelationCreated": False,
            })

        counts = {
            "importBatches": count(conn, "SELECT COUNT(*) FROM import_batch"),
            "sourceProductRows": count(conn, "SELECT COUNT(*) FROM source_row WHERE source_document_id='doc-pr143-products'"),
            "galleryImageAssets": count(conn, "SELECT COUNT(*) FROM image_asset WHERE source_document_id='doc-pr143-gallery'"),
            "galleryImagesVisuallyInspected": sum(r["visualInspectionStatus"] == "inspected" for r in gallery_evidence),
            "galleryReviewGroups": count(conn, "SELECT COUNT(DISTINCT subject_id) FROM evidence_claim WHERE predicate='catalog_reconciliation_disposition'"),
            "crossCheckedGroupEvidenceClaims": count(conn, "SELECT COUNT(*) FROM evidence_claim WHERE predicate='catalog_reconciliation_disposition' AND claim_status='cross_checked'"),
            "hypothesisEvidenceClaims": count(conn, "SELECT COUNT(*) FROM evidence_claim WHERE predicate='catalog_reconciliation_disposition' AND claim_status='hypothesis'"),
            "fullyVerifiedCanonicalProductRecords": count(conn, "SELECT COUNT(*) FROM release WHERE variant_id IS NOT NULL"),
            "canonicalCastings": count(conn, "SELECT COUNT(*) FROM casting"),
            "canonicalVariants": count(conn, "SELECT COUNT(*) FROM variant"),
            "canonicalReleases": count(conn, "SELECT COUNT(*) FROM release"),
            "canonicalAssortments": count(conn, "SELECT COUNT(*) FROM assortment"),
            "imageToEntityRelations": count(conn, "SELECT COUNT(*) FROM image_relation"),
        }
        if len(source_records) != 41 or len(gallery_evidence) != 55:
            raise SystemExit(f"Unexpected source counts: {len(source_records)} product rows, {len(gallery_evidence)} images")
        if counts["galleryImagesVisuallyInspected"] != 55 or counts["imageToEntityRelations"] != 0:
            raise SystemExit("Visual review or no-auto-link invariant failed")
        if any(counts[key] != 0 for key in ("fullyVerifiedCanonicalProductRecords", "canonicalCastings", "canonicalVariants", "canonicalReleases", "canonicalAssortments")):
            raise SystemExit("Unexpected canonical entities appeared in the staged pilot")
        if len(assets) != 55:
            raise SystemExit(f"Expected 55 downloaded WebP files, found {len(assets)}")

        data = {
            "schemaVersion": "1.0.0",
            "generatedFrom": "SQLite queries over database/schema.sql and the three staged pilot seeds; review metadata joined from committed review tables",
            "sourceRepository": "JohnyKiska/hotwheels-fandom-archive",
            "generatedAt": date.today().isoformat(),
            "scope": "Hot Wheels Pro Racing 1:43",
            "databaseState": {
                "importBatches": counts["importBatches"],
                "sourceProductRows": counts["sourceProductRows"],
                "galleryImageAssets": counts["galleryImageAssets"],
                "galleryImagesVisuallyInspected": counts["galleryImagesVisuallyInspected"],
                "galleryReviewGroups": counts["galleryReviewGroups"],
                "crossCheckedGroupEvidenceClaims": counts["crossCheckedGroupEvidenceClaims"],
                "hypothesisEvidenceClaims": counts["hypothesisEvidenceClaims"],
                "fullyVerifiedCanonicalProductRecords": counts["fullyVerifiedCanonicalProductRecords"],
                "canonicalCastings": counts["canonicalCastings"],
                "canonicalVariants": counts["canonicalVariants"],
                "canonicalReleases": counts["canonicalReleases"],
                "canonicalAssortments": counts["canonicalAssortments"],
                "imageToEntityRelations": counts["imageToEntityRelations"],
                "verifiedAncillaryGroups": ["PR143-G04", "PR143-G15"],
            },
            "policy": {
                "publishCanonicalOnlyWhenFullyVerified": True,
                "sourceRowsAreNotCanonicalReleases": True,
                "galleryInspectionDoesNotProveProductIdentity": True,
                "candidateLinksRemainNonCanonical": True,
            },
            "sourceRecords": source_records,
            "galleryEvidence": gallery_evidence,
        }
        OUTPUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"passed": True, "output": str(OUTPUT.relative_to(ROOT)), "counts": counts, "sourceRecords": len(source_records), "galleryEvidence": len(gallery_evidence), "assetsResolved": len(assets)}, ensure_ascii=False, indent=2))
        return 0
    finally:
        conn.close()
        DB.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
