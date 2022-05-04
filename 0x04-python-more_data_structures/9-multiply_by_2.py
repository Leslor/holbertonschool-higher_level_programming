#!/usir/bin/python3


def multiply_by_2(a_dictionary):
    """ function  that returns a new dictionary with values multiplied by 2"""
    values = list(map(lambda value: value * 2, a_dictionary.values()))
    new_dictionary = dict(zip(a_dictionary.keys(),values))
    return new_dictionary
