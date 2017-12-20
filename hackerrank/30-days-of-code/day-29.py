#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    
    print(k-1 if ((k-1) | k) <= n else k-2)
    
    '''
    This solution times out!
    max = 0
    
    for i in range(1, n):
        for j in range(i+1, n+1):
            result = i & j
            if k > result > max:
                max = result
    print(max)
    '''
