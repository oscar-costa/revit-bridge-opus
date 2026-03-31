"""
tests/test_hash.py

Unit tests for computing SHA-256 hash.
"""

import os
import tempfile
from lib.core.hash import compute_file_hash, hashes_match

def test_compute_file_hash():
    # Create temp file with known content
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as tf:
        tf.write("hello world")
        tf_path = tf.name
        
    try:
        # echo -n "hello world" | sha256sum -> b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
        expected_hash = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
        
        computed_hash = compute_file_hash(tf_path)
        assert computed_hash == expected_hash
        assert hashes_match(tf_path, expected_hash)
    finally:
        os.remove(tf_path)
