# CTCI 4.6
# Successor

# Assume each child has a link to its parent
class Node():
  def __init__(self, value, left=None, right=None, parent=None):
    self.value, self.left, self.right, self.parent = value, left, right, parent
    if self.left:  self.left.parent  = self
    if self.right: self.right.parent = self

# My Solution
def successor(root):
    # Check for right subtree
    if root.right is not None:
        # IN ORDER TRAVERSAL ON RIGHT SUBTREE
        # Or just go to the left most node
        temp = root.right
        # Loop until leftmost node on right tree
        while temp.left is not None:
            temp = temp.left
        return temp
        
    elif root.parent is not None:
        # If parent is less than, keep going up
        # This occurs when you are in the right subtree already
        if root.parent.value < root.value:
            temp = root.parent
            # Loop until you find the correct successor or reach None
            while temp and temp.value < root.value:
                temp = temp.parent
            return temp
        # Return the parent, if it is the correct successor
        return root.parent
    return None
        


#-------------------------------------------------------------------------------
#Testing

import unittest

class Test(unittest.TestCase):
  def test_successor(self):
    self.assertEqual(successor(Node(22, Node(11))), None)
    self.assertEqual(successor(Node(22, Node(11), Node(33))).value, 33)
    self.assertEqual(successor(Node(22, Node(11), Node(33, Node(28)))).value, 28)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).left).value, 22)
    self.assertEqual(successor(Node(22, Node(11), Node(33)).right), None)

if __name__ == "__main__":
  unittest.main()