#!/usr/bin/python3
"""Defines a Json-to-object function."""
import json


def from_json_string(my_str):
    """Return the python object rep of a JSON string."""
    return json.loads(my_str)
