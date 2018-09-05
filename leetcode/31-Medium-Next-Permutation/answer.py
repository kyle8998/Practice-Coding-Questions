#!/usr/bin/python

#------------------------------------------------------------------------------

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            swap = None
            min_idx = None
            for i in range(len(nums)-2, -1, -1):
                # If the curr element is less than the right one
                # We want to swap them with the minimum
                if nums[i] < nums[i+1]:
                    swap = i+1
                    
                    # Find the smallest number on the right side that is > curr number then swap
                    for j, n in enumerate(nums[swap:len(nums)]):
                        if not min_idx and nums[i] < n:
                            min_idx = swap+j
                        elif min_idx is not None and nums[i] < n < nums[min_idx]:
                            min_idx = swap+j
                    nums[i], nums[min_idx] = nums[min_idx], nums[i]
                    break
            
            # If list is already in descending order
            if swap is None:
                nums.reverse()
            # We want to sort the right side of the list (swap:end)
            else:
                for n in sorted(nums[swap:len(nums)]):
                    nums[swap] = n
                    swap += 1

#------------------------------------------------------------------------------
#Testing
