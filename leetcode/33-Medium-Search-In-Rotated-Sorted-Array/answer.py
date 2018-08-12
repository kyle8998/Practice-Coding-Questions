#!/usr/bin/python3

#------------------------------------------------------------------------------

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums: return -1
        return self.binary_search(nums, target, 0, len(nums)-1)

    def binary_search(self, nums, target, l, r):
        if l > r: return -1
        mid = (l + r) // 2
        if target == nums[mid]: return mid
        
        # If left side is in the correct order...
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # If left side is fucked we know the right side is okay!
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return self.binary_search(nums, target, l, r)

#------------------------------------------------------------------------------
#Testing
