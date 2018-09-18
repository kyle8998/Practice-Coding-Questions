#!/usr/bin/python3

#------------------------------------------------------------------------------

class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0] or grid[0][0] == 1:
            return 0
        # **NOTE** Cannot use multiplication because it copies references
        # Must use list comprehension for this to create cache
        # cache = [[0]*len(grid[0])]*len(grid)
        cache = [[0]*len(grid[0]) for _ in range(len(grid))]
        cache[0][0] = 1
        
        # Set side paths
        for row in range(1, len(grid)):
            if grid[row][0] == 1:
                break
            cache[row][0] = 1
        for col in range(1, len(grid[0])):
            if grid[0][col] == 1:
                break
            cache[0][col] = 1
        
        # Set rest of cache
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                if grid[row][col] == 0:
                    cache[row][col] = cache[row-1][col] + cache[row][col-1]
        
        return cache[-1][-1]
        
#------------------------------------------------------------------------------
#Testing
