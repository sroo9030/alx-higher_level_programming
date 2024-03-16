#!/usr/bin/python3
# 1-write_file.py
'''Define a function that writes a string to a text file (UTF8)'''


def write_file(filename="", text=""):
    '''a function that writes a string to a text file

    Args:
        filename(file): file to write into
        text(string): the text to write

    Return:
        the number of characters written
    '''
    with open(filename,  mode='w', encoding='utf-8') as f:
        return f.write(text)
