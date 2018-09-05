#!/usr/bin/env python3

#-------------------------------------------------------------------------------
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return -1
        
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow];
            fast = nums[nums[fast]];
            
        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
            
        return slow
#-------------------------------------------------------------------------------
