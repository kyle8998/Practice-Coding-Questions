#!/usr/bin/env python3

#-------------------------------------------------------------------------------

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        if prices:
            low = prices[0]
            for i in prices:
                if i < low:
                    low = i
                elif i - low > profit :
                    profit = i - low
            
        return profit

#-------------------------------------------------------------------------------
# Testing
