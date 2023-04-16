#!/usr/bin/python3
"""Defines a class student."""


class Student:
    """Rep a student."""

    def __init__(self, first_name, last_name, age):
        """Init a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json_self, attrs=None):
        """Get a dictionary representation of the students."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {m: getattr(self, m) for m in attrs if hasattr(self, m)}
        return self.__dict__
