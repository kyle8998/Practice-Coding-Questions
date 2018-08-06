#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Brute Force O(n^2) Solution
#-------------------------------------------------------------------------------
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Really brute force n^2
        pairs = []
        profit = 0
        
        # Find every valid transaction
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > 0:
                    pairs.append((i, j, prices[j] - prices[i]))

        print(pairs)
        for i in range(len(pairs)):
            # Get profit from first transction
            first = pairs[i][2]
            profit = max(profit, first)
            for j in range(i+1, len(pairs)):
                # If valid second transaction
                if pairs[j][0] >= pairs[i][1]:
                    profit = max(profit, first + pairs[j][2])

        return profit
        
#-------------------------------------------------------------------------------
# O(3n) Solution
#-------------------------------------------------------------------------------    
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices)<=1: return 0
        profit = 0
        
        left = [0]*len(prices)
        curr = prices[0]
        # Find max gain from left to right
        for i in range(1, len(prices)):
            curr= min(curr, prices[i])
            left[i] = max(prices[i]-curr, left[i-1])
        
        # Find max gain from right to left
        right = [0]*len(prices)
        curr = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            curr = max(curr, prices[i])
            right[i] = max(curr-prices[i], right[i+1])
        
        # By finding the profit left/right we can determine
        # them to be pairs of transactions. Together they
        # represent the max profit of selling and buying on
        # that day
        for l, r in zip(left, right):
            profit = max(profit, l + r)
            
        return profit

#-------------------------------------------------------------------------------
# Testing
