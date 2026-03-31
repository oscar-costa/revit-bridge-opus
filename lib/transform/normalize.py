"""
lib/transform/normalize.py

Normalizes OPUS data extracted from .opux and .mdb files into the target JSON Schema Format.
Ensures correct types and required fields for concepts and groups.
"""

def normalize_budget(raw_groups, raw_concepts):
    """
    Transforms extracted groups and concepts to the JSON schema format.
    
    Args:
        raw_groups (list of dict): Data extracted from OPUS grouped nodes.
        raw_concepts (list of dict): Data extracted from OPUS items/concepts nodes.
        
    Returns:
        dict: Budget matching the JSON Schema defining 'groups' and 'concepts'.
    """
    groups = []
    concepts = []
    
    for rg in raw_groups:
        group = {
            "id": str(rg.get("id", "")),
            "name": str(rg.get("name", "")),
            "parent_id": str(rg.get("parent_id")) if rg.get("parent_id") is not None else None
        }
        groups.append(group)
        
    for rc in raw_concepts:
        concept = {
            "id": str(rc.get("id", "")),
            "group_id": str(rc.get("group_id", "")),
            "code": str(rc.get("code", "")),
            "description": str(rc.get("description", "")),
            "unit": str(rc.get("unit", "")),
        }
        
        # unit_price is optional
        if "unit_price" in rc and rc["unit_price"] is not None:
            try:
                concept["unit_price"] = float(rc["unit_price"])
            except ValueError:
                pass
                
        concepts.append(concept)
        
    # Budget structure matching budget.schema.json
    budget_data = {
        "groups": groups,
        "concepts": concepts
    }
    
    return budget_data
