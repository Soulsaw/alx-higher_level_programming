#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_1
    names = []
    names = dir(hidden_1)
    for name in names:
        if "__" in name:
            continue
        else:
            print(name)
