#!/usr/bin/env python3

#-------------------------------------------------------------------------------

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        # Keep going until we find the fuckywucky equilibrium
        while l < r:
            mid = (l + r) // 2
            # If right is fucked, go to it
            if nums[mid] > nums[r]:
                l = mid+1
            # If left is fucked, go to it
            else:
                r = mid
        
        return nums[l]

#-------------------------------------------------------------------------------

