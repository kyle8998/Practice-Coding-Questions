#!/bin/python3

import sys


n = int(input().strip())

count = 0
result = 0
for c in str(bin(n)):
    if c == '1':
        count += 1
        result = max(count, result)
    else:
        count = 0
print(result)