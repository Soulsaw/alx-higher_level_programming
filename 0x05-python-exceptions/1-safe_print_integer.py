#!/usr/bin/python3
def safe_print_integer(value):
    boolean = False
    try:
        print("{:d}".format(value))
        boolean = True
    except ValueError:
        boolean = False
    return boolean
