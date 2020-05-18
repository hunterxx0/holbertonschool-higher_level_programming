#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        if isinstance(value, float):
            if value.is_integer():
                print("{:d}".format(int(value)))
                return True
        return False
