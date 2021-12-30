#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    len = len(argv)
    if len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] == '+':
        res = add(int(argv[1]), int(argv[3]))
    elif argv[2] == '-':
        res = sub(int(argv[1]), int(argv[3]))
    elif argv[2] == '*':
        res = mul(int(argv[1]), int(argv[3]))
    elif argv[2] == '/':
        res = div(int(argv[1]), int(argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:} {:d} = {:d}".format(a, argv[2], b, res))
