#!/usr/bin/python3


def roman_to_int(roman_string):
    """Function  that converts a Roman numeral to an integer"""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    ROMAN_NUMERAL = {
        'M': 1000, 'C': 100, 'X': 10,
        'I': 1, 'D': 500, 'L': 50, 'V': 5
    }
    SPECIAL_CASES = {
        'IX': 9, 'XC': 90, 'CM': 900,
        'IV': 4, 'XL': 40, 'CD': 400
    }
    decimal_number, i = 0, 0
    size = len(roman_string)
    while i < size:
        if i < size - 1:
            sp_case = roman_string[i] + roman_string[i+1]
            if sp_case in SPECIAL_CASES.keys():
                decimal_number += SPECIAL_CASES[sp_case]
                i += 2
                continue
        if roman_string[i] in ROMAN_NUMERAL.keys():
            decimal_number += ROMAN_NUMERAL[roman_string[i]]
            i += 1
        else:
            return 0
    return decimal_number
