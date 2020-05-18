#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ls = []
    i = 0
    for i in range(list_length):
        try:
            s = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            s = 0
            print("division by 0")
        except (TypeError):
            s = 0
            print("wrong type")
        except (IndexError):
            s = 0
            print("out of range")
        finally:
            print("", end="")
        ls.append(s)
    return ls
