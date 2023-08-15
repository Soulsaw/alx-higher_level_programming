#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    tuple_a: Is the tuple a
    tuple_b: Is the tuple b
    """
    a, b = tuple_a[0], tuple_a[1]
    for i in range(len(tuple_a)):
        for j in range(len(tuple_b)):
            if i == 0 and j == 0:
                a = tuple_a[i] + tuple_b[j]
                break
            elif i == 1 and j == 1:
                b = tuple_a[i] + tuple_b[j]
                break
    return (a, b)
                
            
    