#!/usr/bin/env python

#-------------------------------------------------------------------------------
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return int((3 * sum(set(nums)) - sum(nums)) / 2)
#-------------------------------------------------------------------------------
# Testing
