-- HW Catalog canonical data model, SQLite reference schema
-- Source CSVs remain immutable. Import source rows before resolving identities.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS import_batch (
  import_batch_id TEXT PRIMARY KEY,
  source_path TEXT NOT NULL,
  source_blob_sha TEXT,
  imported_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  importer_version TEXT,
  status TEXT NOT NULL CHECK (status IN ('staged','validated','committed','rejected')),
  notes TEXT
);

CREATE TABLE IF NOT EXISTS source_document (
  source_document_id TEXT PRIMARY KEY,
  source_path TEXT NOT NULL,
  source_blob_sha TEXT,
  source_url TEXT,
  source_revision_id TEXT,
  retrieved_at TEXT,
  content_sha256 TEXT,
  UNIQUE(source_path, source_blob_sha)
);

CREATE TABLE IF NOT EXISTS source_row (
  source_row_id TEXT PRIMARY KEY,
  source_document_id TEXT NOT NULL REFERENCES source_document(source_document_id),
  source_table_key TEXT,
  source_section TEXT,
  source_row_number INTEGER,
  record_type TEXT,
  raw_headers_json TEXT,
  raw_cells_json TEXT NOT NULL,
  raw_row_html TEXT,
  import_batch_id TEXT REFERENCES import_batch(import_batch_id),
  UNIQUE(source_document_id, source_table_key, source_row_number)
);

CREATE TABLE IF NOT EXISTS casting (
  casting_id TEXT PRIMARY KEY,
  canonical_name TEXT NOT NULL,
  manufacturer TEXT DEFAULT 'Mattel',
  notes TEXT
);

CREATE TABLE IF NOT EXISTS variant (
  variant_id TEXT PRIMARY KEY,
  casting_id TEXT NOT NULL REFERENCES casting(casting_id),
  variant_name TEXT,
  color TEXT,
  tampo TEXT,
  base_color_or_type TEXT,
  window_color TEXT,
  interior_color TEXT,
  wheel_type TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS assortment (
  assortment_id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  assortment_type TEXT,
  year TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS release (
  release_id TEXT PRIMARY KEY,
  variant_id TEXT REFERENCES variant(variant_id),
  assortment_id TEXT REFERENCES assortment(assortment_id),
  release_year TEXT,
  scale TEXT,
  toy_number TEXT,
  series_position TEXT,
  country TEXT,
  packaging_type TEXT,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS assortment_component (
  assortment_id TEXT NOT NULL REFERENCES assortment(assortment_id),
  release_id TEXT NOT NULL REFERENCES release(release_id),
  component_order INTEGER,
  quantity INTEGER DEFAULT 1,
  PRIMARY KEY (assortment_id, release_id)
);

CREATE TABLE IF NOT EXISTS image_asset (
  image_id TEXT PRIMARY KEY,
  file_name TEXT,
  image_key TEXT,
  image_url TEXT,
  file_page_url TEXT,
  image_alt TEXT,
  image_title TEXT,
  caption_html TEXT,
  image_sha256 TEXT,
  media_type TEXT,
  evidence_type TEXT,
  source_document_id TEXT REFERENCES source_document(source_document_id),
  source_row_id TEXT REFERENCES source_row(source_row_id)
);

-- A gallery image can document a casting, a release, an assortment, or remain unassigned.
CREATE TABLE IF NOT EXISTS image_relation (
  image_relation_id TEXT PRIMARY KEY,
  image_id TEXT NOT NULL REFERENCES image_asset(image_id),
  casting_id TEXT REFERENCES casting(casting_id),
  variant_id TEXT REFERENCES variant(variant_id),
  release_id TEXT REFERENCES release(release_id),
  assortment_id TEXT REFERENCES assortment(assortment_id),
  relation_type TEXT NOT NULL,
  confidence TEXT NOT NULL CHECK (confidence IN ('verified','probable','unverified','rejected')),
  basis TEXT NOT NULL,
  reviewed_by TEXT,
  reviewed_at TEXT,
  CHECK (
    (casting_id IS NOT NULL) +
    (variant_id IS NOT NULL) +
    (release_id IS NOT NULL) +
    (assortment_id IS NOT NULL) = 1
  )
);

CREATE TABLE IF NOT EXISTS evidence_claim (
  evidence_claim_id TEXT PRIMARY KEY,
  source_row_id TEXT NOT NULL REFERENCES source_row(source_row_id),
  subject_type TEXT NOT NULL,
  subject_id TEXT,
  predicate TEXT NOT NULL,
  value_text TEXT,
  claim_status TEXT NOT NULL CHECK (claim_status IN ('source_assertion','visually_verified','cross_checked','hypothesis','rejected')),
  confidence TEXT NOT NULL CHECK (confidence IN ('verified','probable','unverified','rejected')),
  reviewer_notes TEXT
);

CREATE INDEX IF NOT EXISTS idx_variant_casting ON variant(casting_id);
CREATE INDEX IF NOT EXISTS idx_release_variant ON release(variant_id);
CREATE INDEX IF NOT EXISTS idx_release_toy_number ON release(toy_number);
CREATE INDEX IF NOT EXISTS idx_image_source ON image_asset(source_document_id);
CREATE INDEX IF NOT EXISTS idx_image_relation_image ON image_relation(image_id);
CREATE INDEX IF NOT EXISTS idx_source_row_document ON source_row(source_document_id);
