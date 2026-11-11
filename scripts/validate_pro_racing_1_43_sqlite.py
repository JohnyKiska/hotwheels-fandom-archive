#!/usr/bin/env python3
"""Execute and validate the Pro Racing 1:43 staged seed in a temporary SQLite DB."""
from __future__ import annotations
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "database" / "schema.sql"
SEED = ROOT / "database" / "pilot" / "pro-racing-1-43-seed.sql"
RECONCILIATION_SEED = ROOT / "database" / "pilot" / "pro-racing-1-43-reconciliation-seed.sql"
CASTING_CANDIDATE_SEED = ROOT / "database" / "pilot" / "pro-racing-1-43-casting-candidates.sql"
DB = ROOT / "pro-racing-1-43-validation.sqlite"

EXPECTED = {
    "import_batch": 2,
    "source_document": 2,
    "product_source_rows": 41,
    "gallery_source_rows": 55,
    "gallery_image_assets": 55,
    "reconciliation_evidence_claims": 55,
    "reconciliation_review_groups": 18,
    "cross_checked_claims": 43,
    "hypothesis_claims": 12,\n    "casting_candidate_claims": 41,\n    "casting_candidate_groups": 18,
}

def scalar(conn: sqlite3.Connection, sql: str) -> int:
    return int(conn.execute(sql).fetchone()[0])

def main() -> int:
    for path in (SCHEMA, SEED, RECONCILIATION_SEED, CASTING_CANDIDATE_SEED):
        if not path.is_file():
            raise SystemExit(f"Required input missing: {path.relative_to(ROOT)}")

    DB.unlink(missing_ok=True)
    report = {"database": "temporary SQLite validation database", "checks": {}, "counts": {}}
    try:
        conn = sqlite3.connect(DB)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript(SCHEMA.read_text(encoding="utf-8"))
        conn.executescript(SEED.read_text(encoding="utf-8"))
        conn.executescript(RECONCILIATION_SEED.read_text(encoding="utf-8"))
        conn.executescript(CASTING_CANDIDATE_SEED.read_text(encoding="utf-8"))

        # Reapply all seeds to verify idempotency.
        conn.executescript(SEED.read_text(encoding="utf-8"))
        conn.executescript(RECONCILIATION_SEED.read_text(encoding="utf-8"))
        conn.executescript(CASTING_CANDIDATE_SEED.read_text(encoding="utf-8"))

        report["counts"] = {
            "import_batch": scalar(conn, "SELECT COUNT(*) FROM import_batch"),
            "source_document": scalar(conn, "SELECT COUNT(*) FROM source_document"),
            "product_source_rows": scalar(conn, "SELECT COUNT(*) FROM source_row WHERE source_document_id='doc-pr143-products'"),
            "gallery_source_rows": scalar(conn, "SELECT COUNT(*) FROM source_row WHERE source_document_id='doc-pr143-gallery'"),
            "gallery_image_assets": scalar(conn, "SELECT COUNT(*) FROM image_asset WHERE source_document_id='doc-pr143-gallery'"),
            "reconciliation_evidence_claims": scalar(conn, "SELECT COUNT(*) FROM evidence_claim WHERE predicate='catalog_reconciliation_disposition'"),
            "reconciliation_review_groups": scalar(conn, "SELECT COUNT(DISTINCT subject_id) FROM evidence_claim WHERE predicate='catalog_reconciliation_disposition'"),
            "cross_checked_claims": scalar(conn, "SELECT COUNT(*) FROM evidence_claim WHERE predicate='catalog_reconciliation_disposition' AND claim_status='cross_checked'"),
            "hypothesis_claims": scalar(conn, "SELECT COUNT(*) FROM evidence_claim WHERE predicate='catalog_reconciliation_disposition' AND claim_status='hypothesis'"),
            "casting_candidate_claims": scalar(conn, "SELECT COUNT(*) FROM evidence_claim WHERE predicate='source_casting_label' AND subject_type='casting_candidate'"),
            "casting_candidate_groups": scalar(conn, "SELECT COUNT(DISTINCT subject_id) FROM evidence_claim WHERE predicate='source_casting_label' AND subject_type='casting_candidate'"),
            "canonical_castings": scalar(conn, "SELECT COUNT(*) FROM casting"),
            "canonical_variants": scalar(conn, "SELECT COUNT(*) FROM variant"),
            "canonical_releases": scalar(conn, "SELECT COUNT(*) FROM release"),
            "image_relations": scalar(conn, "SELECT COUNT(*) FROM image_relation"),
        }
        for key, expected in EXPECTED.items():
            actual = report["counts"][key]
            report["checks"][f"expected_{key}"] = {"expected": expected, "actual": actual, "passed": actual == expected}

        fk_errors = list(conn.execute("PRAGMA foreign_key_check"))
        integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
        report["checks"]["foreign_key_check"] = {"errors": len(fk_errors), "passed": len(fk_errors) == 0}
        report["checks"]["integrity_check"] = {"result": integrity, "passed": integrity == "ok"}
        report["checks"]["idempotent_seed"] = {
            "passed": all(report["counts"][k] == v for k, v in EXPECTED.items())
        }
        report["checks"]["casting_candidates_are_source_assertions_only"] = {
            "passed": scalar(conn, "SELECT COUNT(*) FROM evidence_claim WHERE predicate='source_casting_label' AND (claim_status<>'source_assertion' OR confidence<>'unverified' OR subject_type<>'casting_candidate')") == 0
        }
        report["checks"]["all_reconciliation_claims_are_group_level"] = {
            "passed": scalar(conn, "SELECT COUNT(*) FROM evidence_claim WHERE predicate='catalog_reconciliation_disposition' AND subject_type<>'review_group'") == 0
        }
        report["checks"]["no_canonical_entities_or_links"] = {
            "passed": all(report["counts"][k] == 0 for k in ("canonical_castings", "canonical_variants", "canonical_releases", "image_relations"))
        }
        report["checks"]["batches_remain_staged"] = {
            "passed": scalar(conn, "SELECT COUNT(*) FROM import_batch WHERE status='staged'") == 2
        }
        conn.close()
        report["passed"] = all(item["passed"] for item in report["checks"].values())
        out = ROOT / "database" / "pilot" / "SQLITE-EXECUTION-REPORT.json"
        out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, indent=2))
        return 0 if report["passed"] else 1
    finally:
        DB.unlink(missing_ok=True)

if __name__ == "__main__":
    sys.exit(main())
