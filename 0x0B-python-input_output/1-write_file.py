#!/usr/bin/python3
"""Defines a file-writing fuction."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file."""
    with open(filename, "W", encoding="utf-8") as f:
        return f.write(text)
