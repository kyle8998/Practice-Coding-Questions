#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Optimal Solution O(n)
#-------------------------------------------------------------------------------

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        output = []
        
        # We grow a product from left to right offset by 1
        for i in range(len(nums)):
            output.append(p)
            p *= nums[i]
        
        p = 1
        # Now we grow a product from right to left
        # The product of the two products will be our desired result
        for i in range(len(nums)-1, -1, -1):
            output[i] *= p
            p *= nums[i]
        
        return output

#-------------------------------------------------------------------------------
# O(n) Cheaty Division Way
#-------------------------------------------------------------------------------   
        
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[0]*len(nums)
        zero = nums.count(0)
        if zero >= 2:
            return output
        elif zero == 1:
            i = 0
            while nums[i] != 0:
                i += 1
            p = 1
            for n in nums[:i] + nums[i+1:]:
                p *= n
            output[i] = p
            return output
        else:
            p = 1
            for n in nums:
                p *= n   
            for i in range(len(nums)):
                output[i] = p//nums[i]
            return output
            
#-------------------------------------------------------------------------------
# Simple O(n^2) brute force
#-------------------------------------------------------------------------------

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                output[i] *= nums[j]
        return output
#-------------------------------------------------------------------------------
