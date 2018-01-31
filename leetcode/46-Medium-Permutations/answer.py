#!/usr/bin/python

#------------------------------------------------------------------------------

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        self.helper(nums, [], result)
        return result
            
    def helper(self, nums, curr, result):
        if not nums:
            result.append(curr)
        else:
            for i in range(len(nums)):
                # This removes the element from nums and puts it in curr for the next call
                self.helper(nums[:i]+nums[i+1:], curr+[nums[i]], result)

#------------------------------------------------------------------------------
#Testing
