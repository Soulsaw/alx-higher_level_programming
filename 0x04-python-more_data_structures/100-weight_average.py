#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        prods, sums = 0, 0
        for tuplea in my_list:
            prods += tuplea[0] * tuplea[1]
            sums += tuplea[1]
        return prods / sums
