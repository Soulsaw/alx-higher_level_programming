#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import __name__
    names = []
    names = dir(__name__)
    for name in names:
        if "__" in name:
            continue
        else:
            print(name)
