#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    _arg_len = len(sys.argv)
    if (_arg_len - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operators = "+-*/"
        op = sys.argv[2]
        if op not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            calculs = {'+' : add, '-' : sub, '*' : mul, '/' : div}
            print("{:d} {} {:d} = {}".format(a, op, b, calculs[op](a, b)))
            exit(0)
