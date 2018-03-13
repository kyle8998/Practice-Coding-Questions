# CTCI 4.4
# Check Balanced

import unittest
import math
import sys

class Node():
  def __init__(self, left=None, right=None):
    self.left, self.right = left, right

        

# My Solution

# Uses 99999999 as an error code when not balanced
# Should use max int?
def is_balanced(root):
    return checkHeight(root) != 99999999
    
def checkHeight(root):
    if root is None:
        return -1

    leftHeight = checkHeight(root.left)
    if leftHeight == 99999999:
        return 99999999

    rightHeight = checkHeight(root.right)
    if rightHeight == 99999999:
        return 99999999

    if abs(leftHeight - rightHeight) > 1:
        return 99999999

    return max(leftHeight, rightHeight) +1



# First brute force O(nlogn)
def check_balanced(root):
    if not root:
        return True
    left = get_height(root.left, 0)
    right = get_height(root.right, 0)
    if left == right or left == right+1 or left == right-1:
        return is_balanced(root.left) and is_balanced(root.right)
    return False
    

# Brute force to get height
def get_height(root, height):
    if not root:
        return height
    return max(get_height(root.left, height+1), get_height(root.right, height+1))

    

#-------------------------------------------------------------------------------
# CTCI Solution 


#-------------------------------------------------------------------------------
#Testing

class Test(unittest.TestCase):
  def test_is_balanced(self):
    self.assertEqual(is_balanced(Node(Node(),Node())), True)
    self.assertEqual(is_balanced(Node(Node(),Node(Node()))), True)
    self.assertEqual(is_balanced(Node(Node(),Node(Node(Node())))),
        False)
    self.assertEqual(is_balanced(Node(Node(Node()),Node(Node(Node())))),
        False)
    self.assertEqual(is_balanced(Node(Node(Node()),
        Node(Node(Node()),Node()))), True)

if __name__ == "__main__":
  unittest.main()