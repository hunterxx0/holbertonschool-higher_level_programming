#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv)
    if x == 2:
        print("{}".format(argv[1]))
    elif x == 1:
        print("0")
    else:
        s = 0
        for i in range(1, x):
            s += int(argv[i])
        print("{}".format(s))
