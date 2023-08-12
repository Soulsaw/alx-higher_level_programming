#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    _len = len(sys.argv) - 1
    result = 0
    for i in range(_len):
        result += int(sys.argv[i + 1])
    print("{:d}".format(result))
