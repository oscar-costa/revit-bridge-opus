"""
lib/core/hash.py

File integrity hashing using SHA-256.
Used to detect changes in OPUS source files between imports.
"""

import hashlib
import os


BLOCK_SIZE = 65536  # 64 KB read chunks


def compute_file_hash(file_path):
    """
    Compute the SHA-256 hash of a file.

    Args:
        file_path (str): Absolute path to the file (UNC paths supported).

    Returns:
        str: Hex-encoded SHA-256 digest.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If the file cannot be read.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File not found: {}".format(file_path))

    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        block = f.read(BLOCK_SIZE)
        while block:
            hasher.update(block)
            block = f.read(BLOCK_SIZE)

    return hasher.hexdigest()


def hashes_match(file_path, expected_hash):
    """
    Check whether a file's current hash matches an expected value.

    Args:
        file_path (str): Absolute path to the file.
        expected_hash (str): Previously computed SHA-256 hex digest.

    Returns:
        bool: True if the file is unchanged, False if it has changed.
    """
    return compute_file_hash(file_path) == expected_hash
