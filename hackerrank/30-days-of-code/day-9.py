#!/bin/python3

import sys

def factorial(n):
    # Complete this function
    if n == 1: return n
    else: return n * (factorial(n-1))

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
