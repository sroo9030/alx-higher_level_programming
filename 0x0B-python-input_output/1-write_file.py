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
    count = 0
    with open(filename,  mode='w', encoding='utf-8') as f:
        if text:
            for i in text:
                if i == " " or i == "\n":
                    count += 1
            count += len(text)
        f.write(text)
    return count
