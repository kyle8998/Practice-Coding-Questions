#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# O(n) Space Complexity

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = [0]*(len(nums)+1)
        for n in nums:
            numbers[n] = 1
        for i in range(len(numbers)):
            if numbers[i] == 0:
                return i


#-------------------------------------------------------------------------------
# O(1) Space Complexity using math

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (len(nums) * (len(nums) + 1) // 2) - sum(nums)
#-------------------------------------------------------------------------------
