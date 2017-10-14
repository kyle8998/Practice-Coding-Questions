#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(n):
    print (arr[n-i-1], end=" ")