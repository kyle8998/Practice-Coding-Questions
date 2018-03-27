# CTCI 4.11
# Random Node

#-------------------------------------------------------------------------------
# My Solution
#-------------------------------------------------------------------------------

import random
class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        # Keep track of size of each side
        self.size = 1
        if self.left:
          self.size += self.left.size
        if self.right:
          self.size += self.right.size
    
    def get_random(self):
        self.helper(randint(0, self.size - 1))
        
    def helper(self, rand):
        # If rand number is 0, return root
        if rand == 0:
            return self
        
        # If left exists
        if self.left:
            # If rand number is < left_size
            if rand-1 < self.left.size:
                return self.left.helper(rand-1)
            # If rand number is > left_size
            elif self.right:
                return self.right.helper(rand-1-self.left.size)
        
        # If left size is 0, and right exists
        if self.right:
            return self.right.helper(rand-1)
            
        # If no possible result
        return None



#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):
  def test_get_random_value(self):
    tree = Node(11,Node(21,Node(31),Node(32,Node(41),Node(42,None,Node(51)))),
                   Node(22,Node(33),Node(34)))
    self.assertEqual(tree.helper(0).data, 11)
    self.assertEqual(tree.helper(4).data, 41)
    self.assertEqual(tree.helper(8).data, 33)

if __name__ == "__main__":
  unittest.main()