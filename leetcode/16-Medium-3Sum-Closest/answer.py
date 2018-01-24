#!/usr/bin/python

#------------------------------------------------------------------------------

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        
        result = float('inf')
        
        # Loop through each index, then use two pointers to close in the rest of the array
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            
            while l < r:
                # Current sum of the three elements
                curr_sum = nums[i] + nums[l] + nums[r]
                # If the difference is smaller, make it the result
                if abs(target - curr_sum) < abs(target - result):
                    result = curr_sum
                    
                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
                    
        return result

#------------------------------------------------------------------------------
#Testing



main()
