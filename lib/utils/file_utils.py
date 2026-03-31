"""
lib/utils/file_utils.py

General utility functions for interacting with files and handling basic I/O requirements
in the ETL process of the Revit OPUS Bridge project.
"""

import os
import shutil

def get_file_size(path):
    """
    Get the size of a file in bytes.

    Args:
        path (str): The file path.

    Returns:
        int: File size in bytes.
    """
    if os.path.exists(path):
        return os.path.getsize(path)
    return 0


def copy_file(source_path, destination_path):
    """
    Copy a file to a new destination.

    Args:
        source_path (str): The source file path.
        destination_path (str): The destination file path.

    Returns:
        str: Destination path where the file was successfully copied to.
    """
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")

    # Ensure destination directory exists before copying
    os.makedirs(os.path.dirname(os.path.abspath(destination_path)), exist_ok=True)
    
    shutil.copy2(source_path, destination_path)
    return destination_path


def read_text_file(path, encoding='utf-8'):
    """
    Read text from a local file.

    Args:
        path (str): The file path.
        encoding (str, optional): Text encoding. Defaults to 'utf-8'.

    Returns:
        str: File content as a string.
    """
    if not os.path.exists(path):
         raise FileNotFoundError(f"Text file not found: {path}")

    with open(path, 'r', encoding=encoding) as f:
         return f.read()
