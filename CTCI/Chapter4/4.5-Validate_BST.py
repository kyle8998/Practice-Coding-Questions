# CTCI 4.5
# Validate BST

class Node():
  def __init__(self, value, left=None, right=None):
    self.value, self.left, self.right = value, left, right

# My Solution
def validate(root):
    return helper(root, None, None)
    
def helper(root, min, max):
    if root is None:
        return True
    
    # In order left <= curr < right
    
    if (min is not None and root.value <= min) or (max is not None and root.value > max):
        return False
        
    # If the left child is > the parent return false
    if not helper(root.left, min, root.value):
        return False
    # If the right child is <= the parent return false
    if not helper(root.right, root.value, max):
        return False
        
    return True


#-------------------------------------------------------------------------------
#Testing
import unittest

class Test(unittest.TestCase):
  def test_validate_tree(self):
    self.assertEqual(validate(Node(3,Node(1),Node(8))), True)
    tree1 = Node(5,Node(3,Node(1),Node(4)),Node(7,Node(6),Node(8,None,Node(9))))
    self.assertEqual(validate(tree1), True)
    tree2 = Node(7,Node(3,Node(1),Node(8)),Node(9,Node(8),Node(11)))
    self.assertEqual(validate(tree2), False)

if __name__ == "__main__":
  unittest.main()
