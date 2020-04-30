#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    x = len(argv)
    if x == 2:
        print("{} argument:".format(x-1))
        print("{}: {}".format(x-1, argv[1]))
    elif x == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(x-1))
        for i in range(1, x):
            print("{}: {}".format(i, argv[i]))
