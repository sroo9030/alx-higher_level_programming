#!/usr/bin/python3
# 6-load_from_json_file.py
'''This module define JSON-to-Object function'''
import json


def load_from_json_file(filename):
    '''Load data from a JSON file and create a Python object

    Args:
        filename(str): The name of the JSON file

    Return:
        object: The Python object created from the JSON data
    '''
    with open(filename) as f:
        return json.load(f)
