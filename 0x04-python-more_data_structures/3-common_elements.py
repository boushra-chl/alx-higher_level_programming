#!usr/bin/python3
def common_elements(set_1, set_2):
    common_elements = set()
    for x in set_1:
        if x in set_2:
            common_elements.add(x)
    return common_elements
