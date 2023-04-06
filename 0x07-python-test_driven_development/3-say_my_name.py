#!/usr/bin/python3
"""Define a name-printing fuction."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str): The last name to be printed. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Validate the type of input arguments
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the name
     print("My name is {} {}".format(first_name, last_name))
