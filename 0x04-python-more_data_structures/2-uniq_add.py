#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    uniq_elements = set()
    for x in my_list:
        if x not in uniq_elements:
            uniq_elements.add(x)
            add = add + x
    return add
