#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        letter = 'None'
    else:
        letter = sentence[0]
    my_tuple = (length, letter)
    return my_tuple
