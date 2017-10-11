#!/bin/python3

import sys

N = int(input().strip())

if N % 2 == 1: print("Weird")
else:
    if N >= 2 and N <=5: print("Not Weird")
    if N >= 6 and N <=20: print("Weird")
    if N > 20: print("Not Weird")