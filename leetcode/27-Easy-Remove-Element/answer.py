#!/usr/bin/env python

#-------------------------------------------------------------------------------

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        for i in range(0, len(nums)):
            while(nums[i] == val and i < length):
                length -= 1
                nums[i] = nums[length]
        
        return length

#-------------------------------------------------------------------------------
# Testing
def main():
    x = Solution()
    y = x.removeElement([1,1,1,1,2,3,3], 3)
    print y

main()
