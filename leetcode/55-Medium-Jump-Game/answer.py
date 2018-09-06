#!/usr/bin/python3

#------------------------------------------------------------------------------
# Brute Force O(n^2)
#------------------------------------------------------------------------------

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        valid = [len(nums)-1]
        done = []
        while valid:
            curr = valid.pop(0)
            if curr not in done:
                done.append(curr)
                valid += self.getList(nums, curr)
                if 0 in valid:
                    return True
        return False
    
    def getList(self, nums, idx):
        result = []
        for i in range(0, idx):
            if nums[i] >= (idx - i):
                result.append(i)
        return result
        
#------------------------------------------------------------------------------
# Optimized O(n)
#------------------------------------------------------------------------------

class Solution(object):
    def canJump(self, nums):
        if not nums:
            return False
        curr = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= curr - i:
                curr = i
        return True if not curr else False
        

#------------------------------------------------------------------------------
#Testing
