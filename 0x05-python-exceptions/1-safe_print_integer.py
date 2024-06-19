#!/usr/bin/python3
def safe_print_integer(value):
    try:
        val = int(value)
        if isinstance(val, int):
            print("{:d}".format(value))
            return True
        else:
            return False
    except (ValueError, TypeError):
        return False
