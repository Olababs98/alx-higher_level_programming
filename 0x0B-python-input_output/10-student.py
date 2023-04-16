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
        """Get a dict rep of the student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {z:getattr(self, z) for z in attrs if hasattr(self, z)}
        return self.__dict__
