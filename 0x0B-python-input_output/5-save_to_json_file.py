#!/usr/bin/python3
# 5-save_to_json_file.py
'''This module define an object to a text file representation'''
import json


def save_to_json_file(my_obj, filename):
    '''a function that writes an Object to a text file,
       using a JSON representation
    '''
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
