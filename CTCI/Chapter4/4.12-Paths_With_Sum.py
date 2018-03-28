# CTCI 4.12
# Path With Sum

#-------------------------------------------------------------------------------
# My Solution
#-------------------------------------------------------------------------------


class Node():
    def __init__(self, name, data, left=None, right=None):
        self.name, self.data, self.left, self.right = name, data, left, right
        
        
# Brute force O(N^2)
# There is a O(N) solution done by not repeating work when counting paths that I should add later
def path_sum(root, sum):
    if not root:
        return 0
        
    # Return all the paths from the root and call it on each node
    return count_paths(root, sum, 0) + path_sum(root.left, sum) + path_sum(root.right, sum)
    
def count_paths(root, sum, curr):
    if not root:
        return 0
    
    curr += root.data
    
    total_paths = 0
    # If sum is equal to the running sum
    if curr == sum:
        total_paths += 1
    
    # Continue for left and right tree to find all paths
    total_paths += count_paths(root.left, sum, curr)
    total_paths += count_paths(root.right, sum, curr)
    
    return total_paths


#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):
  def test_paths_with_sum(self):
    bt=Node("A",4,Node("B",-2,Node("D",7),Node("E", 4)),
                  Node("C", 7,Node("F",-1,Node("H",-1),Node("I",2,Node("K",1))),
                              Node("G", 0,None,        Node("J", -2))))
    self.assertEqual(path_sum(bt, 12), 1)
    self.assertEqual(path_sum(bt, 2), 4)
    self.assertEqual(path_sum(bt, 9), 4)

if __name__ == "__main__":
  unittest.main()