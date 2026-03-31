# Manifest Tracking System

Located at `data/opus/manifest.json`.

Revit OPUS Bridge relies on this single source of truth for OPUS-to-Revit linkage.

## Structure 

### `active`
Points to the latest exported JSON filename. e.g. `presupuesto_2026-03-31.json`. Revit queries this active file when cost data is needed.

### `source`
Reference payload ensuring the OPUS file integrity.
- `type`: Either `.opux` or `.mdb`.
- `path`: UNC path preferred, but standard absolute paths supported.
- `hash`: SHA-256 integrity hash. When Revit updates budgets, it verifies this hash.

### `history`
A chronological string array of generated output JSON budgets. Useful for cost comparison and snapshot rollback.
