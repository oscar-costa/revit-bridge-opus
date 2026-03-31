"""
Revit OPUS Bridge - Import tool
Imports OPUS cost estimation files (.opux, .mdb) into a normalized JSON format.
"""

__title__ = "Import OPUS"
__author__ = "Antigravity Generated"
__context__ = "zero-doc"  # Document-independent

import os
import sys
import json
import datetime
from pyrevit import forms
from pyrevit import script

# Setup path so `lib` can be imported
EXTENSION_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PROJECT_ROOT = os.path.dirname(EXTENSION_ROOT)
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

try:
    from lib.core.hash import compute_file_hash
    from lib.core.manifest import ManifestManager
    from lib.core.paths import get_source_type, validate_source_path
    from lib.extract.opux import parse_opux
    from lib.extract.mdb import parse_mdb
    from lib.transform.normalize import normalize_budget
except ImportError as e:
    forms.alert(f"Failed to load core libraries: {e}", exitscript=True)


DATA_DIR = os.path.join(PROJECT_ROOT, "data", "opus")
MANIFEST_PATH = os.path.join(DATA_DIR, "manifest.json")
MANIFEST_SCHEMA_PATH = os.path.join(PROJECT_ROOT, "schemas", "manifest.schema.json")
BUDGET_SCHEMA_PATH = os.path.join(PROJECT_ROOT, "schemas", "budget.schema.json")


def pick_source_file():
    """Prompt the user to select an OPUS file (.opux or .mdb)."""
    return forms.pick_file(
        file_ext="opux|mdb",
        title="Select OPUS file to import"
    )

def generate_budget_filename():
    """Generate a unique filename for the new budget JSON."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M")
    return f"presupuesto_{timestamp}.json"


def main():
    # 1. Ask user for file
    source_file = pick_source_file()
    if not source_file:
        return
    
    if not validate_source_path(source_file):
        forms.alert("Selected file is not a supported OPUS file.", exitscript=True)

    output = script.get_output()
    output.print_md(f"# Importing: `{source_file}`")

    # 2. Extract Data
    source_type = get_source_type(source_file)
    try:
        if source_type == ".opux":
             raw_groups, raw_concepts = parse_opux(source_file)
        elif source_type == ".mdb":
             raw_groups, raw_concepts = parse_mdb(source_file)
             
        output.print_md(f"- Loaded {len(raw_groups)} groups and {len(raw_concepts)} concepts from OPUS")
    except Exception as e:
         forms.alert(f"Error extracting data from source file: {e}", exitscript=True)
         
    # 3. Transform Data
    budget_data = normalize_budget(raw_groups, raw_concepts)
    output.print_md("- Extracted data normalized to schema format.")

    # 4. Hash source
    try:
        source_hash = compute_file_hash(source_file)
    except Exception as e:
         forms.alert(f"Error generating hash from source file: {e}", exitscript=True)

    # 5. Save new budget JSON
    os.makedirs(DATA_DIR, exist_ok=True)
    new_active_filename = generate_budget_filename()
    budget_output_path = os.path.join(DATA_DIR, new_active_filename)

    with open(budget_output_path, 'w', encoding='utf-8') as bf:
        json.dump(budget_data, bf, indent=2, ensure_ascii=False)
        
    output.print_md(f"- Extracted data saved as: `{new_active_filename}`")
    
    # 6. Update manifest
    try:
        manifest_manager = ManifestManager(MANIFEST_PATH, MANIFEST_SCHEMA_PATH)
        manifest_manager.update(new_active_filename, source_type, source_file, source_hash)
        output.print_md("- Added extraction step to manifest `manifest.json`.")
    except Exception as e:
         forms.alert(f"Failed to update manifest: {e}", exitscript=True)
         
    output.print_md("**Import Successful!**")

if __name__ == '__main__':
    main()
