#!/usr/bin/python3
def best_score(a_dictionary):
    """
    """

    big_score = None if a_dictionary is None \
        else a_dictionary[list(a_dictionary)[0]] \
        if len(a_dictionary.keys()) > 0 else None
    if big_score is None:
        return big_score
    for key, value in a_dictionary.items():
        if value >= big_score:
            big_score = value
            keys = key
    return keys
