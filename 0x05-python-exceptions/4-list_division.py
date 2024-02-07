#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_res = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            divisor = my_list_2[i]
            if divisor == 0:
                raise ZeroDivisionError("division by 0")
            my_list_res.append(my_list_1[i] /divisor)
        except TypeError:
            print("wrong type")
            my_list_res.append(0)
        except ZeroDivisionError as e:
            print(e)
            my_list_res.append(0)
        except IndexError as e:
            print(e)
            my_list_res.append(0)
    return my_list_res
