#!/usr/bin/python3
"""Defines a string-to-Json function."""
import json


def to_json_string(my_obj):
    """Return the json rep of a string object."""
    return json.dumps(my_obj)
