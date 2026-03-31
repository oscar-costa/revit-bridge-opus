"""
tests/test_manifest.py

Unit tests for reading, writing, and updating the manifest.json file.
"""

import os
import json
import filecmp
from lib.core.manifest import ManifestManager
from lib.core.manifest import load_schema, validate_manifest
import pytest

SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'schemas', 'manifest.schema.json')


def test_manifest_manager(tmpdir):
    """Test full cycle of manifest logic: create new, update, and get active/source."""
    
    # Init manifest manager pointing to temp location
    manifest_path = os.path.join(str(tmpdir), "manifest.json")
    
    # 1. New manager creates default state
    mgr = ManifestManager(manifest_path, SCHEMA_PATH)
    assert mgr.get_active() == ""
    
    # 2. Update with dummy data
    active_budget = "presupuesto_2026-03-31_1530.json"
    source_type = ".opux"
    source_path = r"\\server\costs\projectX\budget.opux"
    source_hash = "a94f8c3b2d1e4f6a7b8c9d0e12345678"
    
    mgr.update(active_budget, source_type, source_path, source_hash)
    
    # 3. Assert properties updated correctly
    assert mgr.get_active() == active_budget
    assert mgr.get_source_hash() == source_hash
    assert active_budget in mgr.data["history"]
    
    # 4. Check saving/disk logic
    assert os.path.exists(manifest_path)
    
    # 5. Load back from disk
    mgr2 = ManifestManager(manifest_path, SCHEMA_PATH)
    assert mgr2.get_active() == active_budget
    assert mgr2.data["history"] == [active_budget]
