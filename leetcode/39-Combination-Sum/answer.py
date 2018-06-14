#!/usr/bin/python

#------------------------------------------------------------------------------

import copy

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.backtrack([], [], candidates, target, 0)

    # Backtracking
    def backtrack(self, result, prefix, candidates, target, idx):
        if target < 0:
            return
        elif target == 0:
            # Need to make a new object because the prefix array will change
            result.append(copy.deepcopy(prefix))
        else:
            # loop through candidates
            for i in range(idx, len(candidates)):
                prefix.append(candidates[i])
                self.backtrack(result, prefix, candidates, target-candidates[i], i)
                # Remove the candidate from prefix for next iteration
                prefix.remove(candidates[i])
        return result

#------------------------------------------------------------------------------
#Testing
