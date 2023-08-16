#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != type('str'):
        return 0
    result = 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for key in dic:
        for char in roman_string:
            if key == char:
                result += dic[key]
    return result


""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int
'''
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
'''

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))


