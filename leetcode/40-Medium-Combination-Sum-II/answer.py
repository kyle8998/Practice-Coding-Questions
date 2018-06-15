#!/usr/bin/python

#------------------------------------------------------------------------------

import copy

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.backtrack([], [], candidates, target, 0)
        
    def backtrack(self, result, prefix, candidates, target, idx):
        if target < 0:
            return
        elif target == 0:
            result.append(copy.deepcopy(prefix))
        else:
            for i in range(idx, len(candidates)):
                # This prevents duplicate work
                # It will only do a combination once by skipping whenever it is a dupe
                if i > idx and candidates[i] == candidates[i-1]:
                    print(candidates[i])
                    continue
                prefix.append(candidates[i])
                self.backtrack(result, prefix, candidates, target-candidates[i], i+1)
                prefix.remove(candidates[i])
        return result

#------------------------------------------------------------------------------
#Testing
