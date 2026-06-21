#!/usr/bin/python3

def solution(value):
    if value % 2 == 0:
        result = 'variable is a multiple of two'
    elif value % 3 == 0:
        result = 'variable is a multiple of three'
    elif value % 5 == 0:
        result = 'variable is a multiple of five'
    else:
        result = 'variable is not a multiple of 2, 3 and 5'
#    print(result)
    return result

# solution(12)
