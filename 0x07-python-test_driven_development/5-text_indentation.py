#!/usr/bin/python3
"""Defines a text indentation test."""


def text_indentation(text):
    """ prints the given text with two new lines after each occurence '.','?'and ':'."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1

    # test the function
    if __name__ == '__main__':
        text_indentation(12)
