#!/usr/bin/python3

#------------------------------------------------------------------------------
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Each key in pairs will be the sum of the pair
        # Values will be tuples that sum to the key
        pairs = {}
        # Find sums for each pair
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                pair_sum = nums[i] + nums[j]
                if pair_sum in pairs:
                    pairs[pair_sum].append((i,j))
                else:
                    pairs[pair_sum] = [(i,j)]
                    
        result = []
        # Find two pairs that equal the target and append to list
        for pair in pairs:
            value = target - pair
            if value in pairs:
                first = pairs[pair]
                second = pairs[value]
                for (i,j) in first:
                    for (k,l) in second:
                        # Ensure none of the same elements are used
                        # ijkl are indices
                        if i!=k and i!=l and j!=k and j!=l:
                            flist = [nums[i],nums[j],nums[k],nums[l]]
                            # Sort to prevent dups
                            flist.sort()
                            if tuple(flist) not in result:
                                result.append(tuple(flist))
        return result

#------------------------------------------------------------------------------
#Testing
