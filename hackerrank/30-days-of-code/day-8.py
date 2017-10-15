#!/bin/python3

import sys

n = int(input().strip())

dict = {}

for i in range(n):
    arr = input().strip().split(' ')
    dict[arr[0]] = arr[1]

for i in range(n):
    name = input().strip()
    if name in dict:
        print ("%s=%s" % (name, dict[name]))
    else:
        print ("Not found")