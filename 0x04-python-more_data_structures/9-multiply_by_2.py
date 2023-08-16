#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    listkeys = list(new_dic.key())
    for i in listkeys:
        new_dic[i] *= 2
    return new_dic
