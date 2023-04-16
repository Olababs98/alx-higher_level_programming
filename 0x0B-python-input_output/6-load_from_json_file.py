#!/usr/bin/python3
"""Define json file-reading function."""
import json


def load_from_json_file(filename):
    """Create python object from json file."""
    with open(filename) as f:
        return json.load(f)
