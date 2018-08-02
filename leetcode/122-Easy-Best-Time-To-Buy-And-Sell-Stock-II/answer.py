#!/usr/bin/env python3

#-------------------------------------------------------------------------------

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([nxt - curr for curr, nxt in zip(prices[:-1], prices[1:]) if curr < nxt])

#-------------------------------------------------------------------------------
# Testing
