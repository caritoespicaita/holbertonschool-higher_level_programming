#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len = len(sys.argv) - 1
    i = 1
    j = 0
    for argv in range(0, len):
        j = j + int(sys.argv[i])
        i = i + 1
    print(j)
