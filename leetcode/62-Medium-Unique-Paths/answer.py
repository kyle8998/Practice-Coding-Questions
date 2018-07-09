#!/usr/bin/python3

#------------------------------------------------------------------------------

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Create the grid to keep track of paths
        grid = [[0]*n for _ in range(m)]
        # Iterate through each path
        for i in range(m):
            for j in range(n):
                # If start (i==0 or j==0) set to 1
                if not i or not j:
                    grid[i][j] = 1
                else:
                    # Sum up the possible paths reaching this spot
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[m-1][n-1]
        

#------------------------------------------------------------------------------
#Testing
