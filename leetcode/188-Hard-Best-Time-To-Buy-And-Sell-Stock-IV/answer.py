#!/usr/bin/env python3

#-------------------------------------------------------------------------------

class Solution:
    def maxProfit_as_many_transactions(self, prices):
        if not prices:
            return 0
        profit, prev = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                profit = profit + prices[i]-prices[i-1]
        return profit
    
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1 or k == 0: return 0
        
        k = min(k, len(prices)-1)
        
        if k >= len(prices) - 1:
            return self.maxProfit_as_many_transactions(prices)
        
        # Create 2d array
        maxes = []
        for _ in range(k+1):
            maxes.append([0]*len(prices))
                
        # Set values in 2d array of max profits
        # k -> number of transactions
        # i -> the current day
        for k in range(1, k+1):
            curr = -prices[0]
            for i in range(1, len(prices)):
                maxes[k][i] = max(maxes[k][i-1], curr + prices[i])
                curr = max(curr, maxes[k-1][i-1] - prices[i])
    
        return maxes[k][len(prices)-1]   

#-------------------------------------------------------------------------------
# Testing
