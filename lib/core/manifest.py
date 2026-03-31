"""
lib/core/manifest.py

Manages the manifest.json file, which tracks the active budget,
source OPUS file integrity, and history of generated files.
"""

import json
import os
import jsonschema


def load_schema(schema_path):
    """Load a JSON schema from a file."""
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_manifest(manifest_data, schema):
    """Validate manifest data against the schema."""
    jsonschema.validate(instance=manifest_data, schema=schema)


class ManifestManager:
    """Manages reading, updating, and writing the manifest.json file."""

    def __init__(self, manifest_path, schema_path):
        """
        Initialize the ManifestManager.

        Args:
            manifest_path (str): Path to the manifest.json file.
            schema_path (str): Path to the manifest.schema.json file.
        """
        self.manifest_path = manifest_path
        self.schema = load_schema(schema_path)
        self.data = self._load()

    def _load(self):
        """Load the manifest.json file if it exists, else return a default structure."""
        if os.path.exists(self.manifest_path):
            with open(self.manifest_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                validate_manifest(data, self.schema)
                return data
        return {
            "active": "",
            "source": {
                "type": "",
                "path": "",
                "hash": ""
            },
            "history": []
        }

    def save(self):
        """Save the current state to the manifest.json file."""
        validate_manifest(self.data, self.schema)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(os.path.abspath(self.manifest_path)), exist_ok=True)
        
        with open(self.manifest_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def update(self, active_budget, source_type, source_path, source_hash):
        """
        Update the manifest with new budget and source information.

        Args:
            active_budget (str): The filename of the newly generated active budget JSON.
            source_type (str): The type of the source file ('.opux' or '.mdb').
            source_path (str): The path to the source file.
            source_hash (str): The SHA-256 hash of the source file.
        """
        self.data["active"] = active_budget
        self.data["source"] = {
            "type": source_type,
            "path": source_path,
            "hash": source_hash
        }
        
        if active_budget not in self.data["history"]:
            self.data["history"].append(active_budget)
            
        self.save()

    def get_active(self):
        """Return the active budget filename."""
        return self.data.get("active")

    def get_source_hash(self):
        """Return the expected SHA-256 hash of the source file."""
        return self.data.get("source", {}).get("hash")
