#!/usr/bin/python3

#-------------------------------------------------------------------------------

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        need = {}
        for i in range(len(nums)):
            if nums[i] in need:
                return [need[nums[i]], i]
            else:
                need[target-nums[i]] = i
        
#-------------------------------------------------------------------------------
