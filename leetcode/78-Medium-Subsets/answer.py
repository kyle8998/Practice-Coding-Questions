#!/usr/bin/python3

#------------------------------------------------------------------------------
# Backtracking Solution
#------------------------------------------------------------------------------

import copy
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(curr, idx):
            for j in range(idx, len(nums)):
                curr.append(nums[j])
                if curr not in power_set:
                    power_set.append(copy.deepcopy(curr))
                    helper(curr, j+1)
                curr.pop()

        power_set = [[]]
        helper([], 0)
                
        return power_set
