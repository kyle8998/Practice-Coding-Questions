#!/usr/bin/python3

#------------------------------------------------------------------------------

from collections import defaultdict
from copy import deepcopy

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        freq_list = self.freq(nums)
        return self.backtrack([], nums, [], freq_list, len(nums))

    # Build freq list
    def freq(self, nums):
        freq_list = defaultdict(int)
        for n in nums:
            freq_list[n] += 1
        return freq_list


    def backtrack(self, result, nums, prefix, freq, remaining):
        if remaining == 0:
            result.append(deepcopy(prefix))
            return result

        # Handles dups because its a dict
        for n in freq:
            if freq[n] > 0:
                # Backtracking
                freq[n] -= 1
                self.backtrack(result, nums, prefix+[n], freq, remaining-1)
                freq[n] += 1

        return result

#------------------------------------------------------------------------------
#Testing
