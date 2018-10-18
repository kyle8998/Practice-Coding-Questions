#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Logarithmic Time
#-------------------------------------------------------------------------------

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        low, high = 0, len(nums) - 1
        while low <= high:
            if low == high:
                return low
            mid = (low + high) // 2
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid

        return mid

#-------------------------------------------------------------------------------
# Linear Time
#-------------------------------------------------------------------------------
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i  
        if nums[-1] > nums[-2]:
            return len(nums)-1
        return None
#-------------------------------------------------------------------------------

