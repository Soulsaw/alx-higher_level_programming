#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    _len = len(sys.argv) - 1
    if (_len == 1):
        print("{} argument:".format(_len))
    else:
        if _len > 0:
            print("{} arguments:".format(_len))
        else:
            print("{} arguments.".format(_len))
    for i in range(_len):
        print("{:d}: {}".format(i + 1, sys.argv[i + 1]))
