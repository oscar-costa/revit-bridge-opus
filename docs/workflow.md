# Workflow

## Importing a Budget

1. The user launches the pyRevit extension tab: **Revit OPUS Bridge**.
2. They click the **Import OPUS** pushbutton.
3. The system raises an OS dialog prompt, letting them pick an `.opux` or `.mdb` file.
4. The backend process scans the file, extracting:
    - Budget Groups
    - Budget Items (Concepts)
5. The budget structure is normalized against the `budget.schema.json`.
6. Output JSON file is dumped into the active Revit Project directory under a `data/opus/` folder.
7. `manifest.json` is updated to reflect the new active budget JSON configuration.

## Cost Update Validation

When a user works with Revit elements and queries the budget database, they do not interact directly with OPUS files. Instead, they interact with the active JSON snapshot linked in the `manifest.json`.
