#!/usr/bin/python3
"""Defines a python class to json function."""


def class_to_json(obj):
    """Return the dic rep of a simple data structure."""
    return obj.__dict__
