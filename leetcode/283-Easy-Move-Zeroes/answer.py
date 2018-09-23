#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# solution

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for num in nums[::-1]:
            if num == 0:
                nums.remove(0)
                nums.append(0)
#-------------------------------------------------------------------------------
