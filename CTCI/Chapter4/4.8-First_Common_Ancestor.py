# CTCI 4.8
# First Common Ancestor

#-------------------------------------------------------------------------------
# My Solution
#-------------------------------------------------------------------------------

class Node():
  def __init__(self, data=None, left=None, right=None):
    self.data, self.left, self.right = data, left, right
      

def fca(root, p, q):
    # First checks if the nodes exist in the root
    if not contains(root, p) or not contains(root, q):
        return None
    return helper(root, p, q)
    
# Helper if tree contains a node
def contains(root, p):
    if root is None:
        return False
    if root == p:
        return True
    
    return contains(root.left, p) or contains(root.right, p)
    
def helper(root, p , q):
    if root is None or root == p or root == q:
        return root
        
    # Check if p/q are on the left side
    p_left = contains(root.left, p)
    q_left = contains(root.left, q)
    
    # If p and q are on opposite sides
    if p_left != q_left:
        return root
    # Both on left side
    elif p_left:
        return helper(root.left, p, q)
    # Both on right side
    else:
        return helper(root.right, p, q)


#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):
  def test_first_common_ancestor(self):
    node1 = Node(11, Node(55), Node(77, Node(44)))
    node2 = Node(22, Node(99))
    self.assertEqual(fca(node1, node1, node2), None)
    node3 = Node(33, node1, Node(88, Node(123, None, node2)))
    node4 = Node(44, node3, Node(66))
    self.assertEqual(fca(node3, node1, node2), node3)

if __name__ == "__main__":
  unittest.main()