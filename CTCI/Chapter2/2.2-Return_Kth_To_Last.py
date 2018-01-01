# CTCI 2.2
# Remove Kth to Last

import unittest
#from LinkedList import LinkedList

# My Solution

def kth_to_last(head, k):
    end = curr = head
    index = curr_idx = 0
    
    # Iterate through ll
    while end is not None:
        end = end.next
        index += 1
        
    # Find index (-1 because it is kth to end. e.g. 2nd to last should only be -1)
    #if k != 0 and k != 1:
    #    index -= (k - 1)
    # Or maybe I'm thinking too much
    index -= k
        
    if index < 0:
        return None
    
    while curr is not None:
        if curr_idx == index:
            return curr
        curr = curr.next
        curr_idx += 1

#-------------------------------------------------------------------------------
# CTCI Solution
# Double pointer!

def akth_to_last(head, k):
    runner = current = head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current

#-------------------------------------------------------------------------------
#Testing

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

class Test(unittest.TestCase):
  def test_kth_to_last(self):
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
    self.assertEqual(None, kth_to_last(head, 0));
    self.assertEqual(7, kth_to_last(head, 1).data);
    self.assertEqual(4, kth_to_last(head, 4).data);
    self.assertEqual(2, kth_to_last(head, 6).data);
    self.assertEqual(1, kth_to_last(head, 7).data);
    self.assertEqual(None, kth_to_last(head, 8));

if __name__ == "__main__":
  unittest.main()