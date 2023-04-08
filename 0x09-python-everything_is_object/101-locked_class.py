#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    prevent users from creating new attributes for the LockedClass 
    except for the attribute named 'first_name'.
    """

    __slots__ = ["first_name"]
