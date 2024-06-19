#!/usr/bin/python3
# 0-read_file.py
"""Define a function that reads a text file (UTF8)"""


def read_file(filename=""):
    """ a finction reads file and prints it to stdout

    Args:
        filename(file): the file tp read
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
