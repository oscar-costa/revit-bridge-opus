"""
lib/core/paths.py

Path utilities to enforce UNC paths for network resilience and validate OPUS paths.
Network drives (like Z:) can be problematic in Revit, so UNC is preferred.
"""

import os
import re

def is_unc_path(path):
    """
    Check if a path is a Windows UNC path.

    Args:
        path (str): The file path to check.

    Returns:
        bool: True if it's a UNC path, False otherwise.
    """
    if not path:
        return False
    # Check for \\server\share format
    return path.startswith(r"\\") or path.startswith("//")


def validate_source_path(path):
    """
    Check if the path has a supported OPUS extension.

    Args:
        path (str): The file path.

    Returns:
        bool: True if it points to .opux or .mdb.
    """
    if not path:
        return False
    ext = os.path.splitext(path)[1].lower()
    return ext in [".opux", ".mdb"]


def get_source_type(path):
    """
    Get the type of the OPUS file based on its extension.

    Args:
        path (str): The file path.

    Returns:
        str: '.opux' or '.mdb' or raises ValueError.

    Raises:
        ValueError: If path extension is not supported.
    """
    if not validate_source_path(path):
        raise ValueError(f"Unsupported OPUS file type: {path}")
    
    return os.path.splitext(path)[1].lower()


def get_absolute_path(path):
    """
    Return the absolute path of a file.

    Args:
        path (str): The file path.

    Returns:
        str: Absolute path.
    """
    return os.path.abspath(path)
