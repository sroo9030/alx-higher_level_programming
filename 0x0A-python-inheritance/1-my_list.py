#!/usr/bin/python3
# 1-my_list.py
"""Define derived class"""


class MyList(list):
    """Represent the derived class"""
    pass

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""

        print(sorted(list(self)))
