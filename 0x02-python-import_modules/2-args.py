#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len = len(sys.argv)
    i = 1
    if len == 1:
        print("{:d} arguments.".format(len - 1))
    elif len == 2:
        print("{:d} argument:".format(len - 1))
        print("1: {:}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(len - 1))
        for argv in range(1, len):
            print("{:d}:".format(i), sys.argv[i])
            i = i + 1
