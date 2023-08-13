#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    _len = len(dir(hidden_4))

    for i in range(_len):
        print("{}".format(dir(hidden_4)[i]))
