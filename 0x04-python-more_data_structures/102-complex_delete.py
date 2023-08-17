#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    """
    new_dic = {}
    for key, values in a_dictionary.items():
        if values is value:
            new_dic[key] = values
    for key, value in new_dic.items():
        if key in a_dictionary:
            del a_dictionary[key]
    return a_dictionary
