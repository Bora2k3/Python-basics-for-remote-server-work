#!/usr/bin/python3

def solution(value):
    if value < 2:
        result = 0
    else:
        result = list(range(value))
        result[1] = 0
        for i in result[2:]:
            for j in range(i + i, len(result), i):
                result[j] = 0
        result = sum(result)
#    print(result)
    return result
#solution(101)
