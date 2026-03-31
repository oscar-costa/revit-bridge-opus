"""
tests/test_normalize.py

Unit tests for data normalization into budget schema.
"""

from lib.transform.normalize import normalize_budget

def test_normalize_budget():
    """Ensure raw extracts map correctly to standard JSON structure."""
    
    raw_groups = [
        {"id": 1, "name": "Preliminaries", "parent_id": None},
        {"id": 2, "name": "Site Prep", "parent_id": 1}
    ]
    
    raw_concepts = [
        {"id": 100, "group_id": 2, "code": "SP-01", "description": "Clearing and grubbing", "unit": "m2", "unit_price": 45.50},
        {"id": 101, "group_id": 2, "code": "SP-02", "description": "Excavation", "unit": "m3", "unit_price": None} # e.g. section header missing price
    ]
    
    budget = normalize_budget(raw_groups, raw_concepts)
    
    # Check structures
    assert len(budget["groups"]) == 2
    assert len(budget["concepts"]) == 2
    
    # Check typing and string casts
    assert budget["groups"][0]["id"] == "1"
    assert budget["groups"][0]["name"] == "Preliminaries"
    assert budget["groups"][0]["parent_id"] is None
    
    assert budget["groups"][1]["parent_id"] == "1"
    
    assert budget["concepts"][0]["unit_price"] == 45.50
    assert "unit_price" not in budget["concepts"][1] # Should gracefully drop 'None'
