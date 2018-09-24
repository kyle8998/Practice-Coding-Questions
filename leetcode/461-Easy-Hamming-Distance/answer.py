#!/usr/bin/env python3

#-------------------------------------------------------------------------------
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x >= y:
            x = bin(x)[2:]
            y = bin(y)[2:].zfill(len(x))
        else:
            y = bin(y)[2:]
            x = bin(x)[2:].zfill(len(y))
        
        count = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
                
        return count
#-------------------------------------------------------------------------------
# Testing
