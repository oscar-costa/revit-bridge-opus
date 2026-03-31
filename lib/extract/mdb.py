"""
lib/extract/mdb.py

Parses data from .mdb (Microsoft Access) files using pyodbc.
Note: Requires Microsoft Access ODBC Driver (64-bit).
"""

import pyodbc
import os

def parse_mdb(file_path):
    """
    Connects to an .mdb file, runs queries to extract groups and concepts.
    
    Args:
        file_path (str): The path to the .mdb file.
        
    Returns:
        tuple: lists of `raw_groups` and `raw_concepts`.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Database not found: {file_path}")

    # Connection string for Microsoft Access Driver
    # (Must be 64-bit for 64-bit Python/Revit versions)
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        rf'DBQ={file_path};'
    )
    
    raw_groups = []
    raw_concepts = []

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        # MDB schema extraction is typically custom based on OPUS versions.
        # Placeholder tables: `tblGroups`, `tblConcepts`
        
        # Determine table names or schema auto-detection logic goes here.
        # Assuming tblGroups / tblConcepts exist...
        # Fallbacks to empty tables to allow testing.

        # Fetch groups
        try:
            cursor.execute("SELECT id, name, parent_id FROM tblGroups")
            for row in cursor.fetchall():
                raw_groups.append({
                    "id": row.id,
                    "name": row.name,
                    "parent_id": row.parent_id
                })
        except pyodbc.Error:
            print("tblGroups not found or schema changed.")

        # Fetch concepts
        try:
            cursor.execute("SELECT id, group_id, code, description, unit, price FROM tblConcepts")
            for row in cursor.fetchall():
               raw_concepts.append({
                    "id": row.id,
                    "group_id": row.group_id,
                    "code": row.code,
                    "description": row.description,
                    "unit": row.unit,
                    "unit_price": row.price
                })
        except pyodbc.Error:
            print("tblConcepts not found or schema changed.")

    except pyodbc.Error as e:
        raise ConnectionError(f"Failed to connect to MDB via ODBC. Error: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

    return raw_groups, raw_concepts
