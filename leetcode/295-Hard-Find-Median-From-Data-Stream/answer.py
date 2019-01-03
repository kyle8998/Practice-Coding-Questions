#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Optimal 2 Heap O(1) Solution
#-------------------------------------------------------------------------------

from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # Create two heaps.
        # One to keep track of the smaller half and one to keep track of the larger half
        self.small = [] # Max Heap
        self.large = [] # Min Heap
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # If heaps are equal size add appropriate element to large heap
        # To determine what element to put in large heap, first we must compare and extract
        # the greatest element in the small heap
        #
        # Note: Negative values in small heap because we want it to mimic the behavior of a max heap
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        

    def findMedian(self):
        """
        :rtype: float
        """
        # If heaps uneven, find mean. Otherwise just remove first element in bigger heap.
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
#-------------------------------------------------------------------------------
# NAIVE SORTING SOLUTION O(nlogn)
#-------------------------------------------------------------------------------
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.nums.append(num)

    def findMedian(self):
        """
        :rtype: float
        """
        self.nums.sort()
        if len(self.nums) == 0:
            return None
        elif len(self.nums) % 2 == 1:
            return float(self.nums[len(self.nums)//2])
        else:
            return (self.nums[len(self.nums)//2] + self.nums[(len(self.nums)//2)-1]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
#-------------------------------------------------------------------------------
