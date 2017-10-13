#!/bin/python3

import sys

N = int(input())
for i in range(0, N):

    string = input()

    for i in range(0, len(string), 2):
        print(string[i], end='')
    print(" ", end='')
    for i in range(1, len(string), 2):
        print(string[i], end='')
    print("")