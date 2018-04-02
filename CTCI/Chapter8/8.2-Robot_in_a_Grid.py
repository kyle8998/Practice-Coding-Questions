# CTCI 8.2
# Robot in a Grid

#-------------------------------------------------------------------------------
# My Solution
#-------------------------------------------------------------------------------
# BRUTE FORCE O(2^x+y)
#-------------------------------------------------------------------------------
def get_path_brute(grid):
    if grid is None or len(grid) == 0:
        return None
    path = []
    if helper(grid, len(grid)-1, len(grid[0])-1, path):
        return path
    return None
    
def helper_brute(grid, row, col, path):
    if row < 0 or col < 0 or grid[row][col] is None:
        return False
        
    # If at origin then the path has made it all the way!
    if (row == 0 and col == 0) or helper_brute(grid, row-1, col, path) or helper_brute(grid, row, col-1, path):
        path.append((row,col))
        return True
        
    return False
    
#-------------------------------------------------------------------------------
# DYNAMIC PROGRAMMING O(XY)
#-------------------------------------------------------------------------------
def get_path(grid):
    if grid is None or len(grid) == 0:
        return None
    path = []
    failed = []
    if helper(grid, len(grid)-1, len(grid[0])-1, path, failed):
        return path
    return None
    
def helper(grid, row, col, path, failed):
    if row < 0 or col < 0 or grid[row][col] is None:
        return False
        
    point = (row,col)
    
    # Already visited this and failed!
    if point in failed:
        return False
        
    # If at origin then the path has made it all the way!
    if point == (0,0) or helper(grid, row-1, col, path, failed) or helper(grid, row, col-1, path, failed):
        path.append(point)
        return True
        
    failed.append(point)
    return False
    

#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):
  def test_path_through_grid(self):
    grid = [[0, 0, 0, 0, 0, 0, None],
            [0, None, None, 0, None, None, 0],
            [0, 0, None, 0, 0, 0, 0],
            [None, None, 0, 0, 0, None, 0]]
    print(get_path(grid))
    
if __name__ == "__main__":
  unittest.main()