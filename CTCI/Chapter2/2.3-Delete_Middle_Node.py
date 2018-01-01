# CTCI 2.3
# Remove Delete Middle Node

import unittest
#from LinkedList import LinkedList

# My Solution
# My approach was to simply shift over every element
# A slightly better approach would be to just delete the next node after shifting it over once

def delete_middle(curr):
    if curr is not None and curr.next is not None:
        curr.data = curr.next.data
        delete_middle(curr.next)
    else:
        curr = None


#-------------------------------------------------------------------------------
# CTCI Solution
# Should have null checks?

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next

#-------------------------------------------------------------------------------
#Testing

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

class Test(unittest.TestCase):
  def test_delete_middle(self):
    head = Node(1,Node(2,Node(3,Node(4))))
    delete_middle(head.next.next)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 2)
    self.assertEqual(head.next.next.data, 4)

if __name__ == "__main__":
  unittest.main()