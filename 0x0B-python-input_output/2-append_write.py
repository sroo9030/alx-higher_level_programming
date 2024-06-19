#!/usr/bin/python3
# 2-append_write.py
'''Define a function that appends a string'''


def append_write(filename="", text=""):
    '''function appends a string at the end of a text file (UTF8)
    '''
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
