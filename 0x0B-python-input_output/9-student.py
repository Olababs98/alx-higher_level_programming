#!/usr/bin/python3
"""Defines a class student."""


class student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dic rep of the student."""
        return self.__dict__
