#!/usr/bin/python3
"""Defines a class student."""


class Student:
    """Rep a student."""

    def __init__(self, first_name, last_name, age):
        """Init a new student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary rep of the student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {g: getattr(self, g) for g in attrs if hasattr(self, g)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student."""
        for g, v in json.items():
            setattr(self, g, v)
