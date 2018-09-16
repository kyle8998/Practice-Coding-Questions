#!/usr/bin/python3

#------------------------------------------------------------------------------
# Brute Force Solution
#------------------------------------------------------------------------------

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        return self.helper(grid, 0, 0, 0)
        
    def helper(self, grid, row, col, path):
        if row == len(grid)-1 and col == len(grid[0])-1:
            return path + grid[row][col]
        elif row == len(grid)-1:
            return self.helper(grid, row, col+1, path + grid[row][col])
        elif col == len(grid[0])-1:
            return self.helper(grid, row+1, col, path + grid[row][col])
        return min(self.helper(grid, row, col+1, path + grid[row][col]),
                  self.helper(grid, row+1, col, path + grid[row][col]))
        
#------------------------------------------------------------------------------
# Optimal Solution (DP)
#------------------------------------------------------------------------------

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # If length of list is 0 return 0
        if not grid or not grid[0]: return 0
        # Create cache to store paths
        cache = [[0]*len(grid[0])]*len(grid)
        
        # Fill in the cache using the minimum path for each element
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == col == 0:
                    cache[0][0] = grid[0][0]
                elif row == 0:
                    cache[row][col] = cache[row][col-1] + grid[row][col]
                elif col == 0:
                    cache[row][col] = cache[row-1][col] + grid[row][col]
                else:
                    cache[row][col] = min(cache[row-1][col], cache[row][col-1]) + grid[row][col]
        # Return the bottom left corner which represents the minimum path to that position
        return cache[-1][-1]
