#!/usr/bin/env python3

#-------------------------------------------------------------------------------
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    self.floodFill(grid, row, col, visited)
                    
        return count
        
    def floodFill(self, grid, row, col, visited):
        neighbors = [(row, col)]
        while neighbors:
            row, col = neighbors.pop()
            visited[row][col] = 1
            # If land
            if grid[row][col] == "1":
                grid[row][col] = "2"
                if row-1 >= 0 and visited[row-1][col] == 0:
                    neighbors.append((row-1, col))
                if row+1 < len(grid) and visited[row+1][col] == 0:
                    neighbors.append((row+1, col))
                if col-1 >= 0 and visited[row][col-1] == 0:
                    neighbors.append((row, col-1))
                if col+1 < len(grid[0]) and visited[row][col+1] == 0:
                    neighbors.append((row, col+1))
        
#-------------------------------------------------------------------------------

