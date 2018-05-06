#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Cheaty Python way :)
# Other way would be to add each digit bit by bit, and having a carry bit when > 1
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        # Sum the two by converting to int
        sum = int(a,2)+int(b,2)
        # Convert back to binary and return excluding the leading '0b'
        return(bin(sum)[2:])
#-------------------------------------------------------------------------------
# Testing
