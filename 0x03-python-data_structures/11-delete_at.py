#!/usr/bin/python3

def delete_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return my_list
    if idx == len(my_list) - 1:
        return my_list[:idx]
    else:
        return my_list[:idx] + my_list[idx + 1:]
