#!/bin/python3

from math import sqrt
num_elements = int(input())

for num in range(num_elements):
    n = int(input())
    prime = True
    if n >= 2:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                prime = False
                break
    else: prime = False
    if prime: print('Prime')
    else: print('Not prime')