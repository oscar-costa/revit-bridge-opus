# Architecture

Revit OPUS Bridge uses a decoupled ETL architecture:

1. **Extract**: Reads `.opux` (XML inside ZIP) or `.mdb` (MS Access) without relying on Revit APIs. Uses Python standard libraries like `xml.etree` and `zipfile` for .opux and `pyodbc` for .mdb. 
2. **Transform**: Normalizes raw extracted groups and items into a clean JSON Schema (`schemas/budget.schema.json`). Uses pure functional logic to convert types and validate structures.
3. **Load (Integration)**: Done mostly by pyRevit via `script.py`. pyRevit is responsible for prompting the user, managing the tool execution across the ETL phases and updating the `manifest.json`.

## Core Libraries

- `lib.core.manifest`: Single source of truth for tracking active budgets and source integrity.
- `lib.core.hash`: File integrity checking.
- `lib.transform.normalize`: Dictionary transformation.
- `lib.extract.*`: OPUS-specific data adapters.
