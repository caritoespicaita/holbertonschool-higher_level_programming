#!/usr/bin/python3
def multiple_returns(sentence):
    len = len(sentences)
    if len == 0:
        letter = 'None'
    else:
        letter = sentence[0]
    my_tuple = (len,letter)
    return my_tuple
