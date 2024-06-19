#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for val in range(0, x):
        try:
            print("{:d}".format(my_list[val]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
