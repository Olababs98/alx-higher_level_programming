#!/usr/bin/python3
"""Defines a text indentation test."""


def text_indentation(text):
    """ prints the given text with two new lines after each occurence '.','?'and ':'."""

    # Validate the type of input argument
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize the output string
    output = ""

    # Loop through each character of the input string
    for char in text:
    # Add the character to the output string
    output += char

    # If the character is '.', '?' or ':', add two new lines to the output string
    if char in ('.', '?', ':'):
        output += "\n\n"

    # Print the output string
    print(output.strip())
