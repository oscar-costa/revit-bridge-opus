"""
lib/extract/opux.py

Parses data from .opux OPUS files.
Assumes .opux files contain XML-structured data (budget groups and items).
"""

import xml.etree.ElementTree as ET
import zipfile
import tempfile
import os

def parse_opux(file_path):
    """
    Parses an .opux file to extract groups and concepts.
    
    Args:
        file_path (str): The path to the .opux file.
        
    Returns:
        tuple: lists of `raw_groups` and `raw_concepts` representing the budget structure.
    """
    raw_groups = []
    raw_concepts = []

    # OPUX files can be XML directly or ZIP archives containing XML.
    if zipfile.is_zipfile(file_path):
         with zipfile.ZipFile(file_path, 'r') as zf:
             # Find the main XML file. For now, picking the first XML file found.
             xml_files = [f for f in zf.namelist() if f.endswith('.xml')]
             if not xml_files:
                  raise ValueError("No XML file found inside the .opux archive.")
             
             with zf.open(xml_files[0]) as xml_file:
                  tree = ET.parse(xml_file)
    else:
        # Assuming plain XML (if OPUS exports raw XML with .opux extension)
         tree = ET.parse(file_path)

    root = tree.getroot()

    # NOTE: The actual XPath/structure depends on the exact OPUS schema.
    # This provides a generic structure for parsing groups and items based on roadmap item: 
    # "[ ] XML parser refinement for .opux"
    
    # Placeholder: mock extracting groups and items based on an assumed 'Node' element
    # Modify XPaths as the schema definition becomes mature.
    for element in root.findall(".//Group"): 
        raw_groups.append({
            "id": element.get("id"),
            "name": element.get("name"),
            "parent_id": element.get("parent_id")
        })

    for element in root.findall(".//Concept"):
        raw_concepts.append({
            "id": element.get("id"),
            "group_id": element.get("group_id"),
            "code": element.get("code"),
            "description": element.get("description"),
            "unit": element.get("unit"),
            "unit_price": element.get("price")
        })

    return raw_groups, raw_concepts
