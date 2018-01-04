# CTCI 2.8
# Loop Detection

import unittest
#from LinkedList import LinkedList

# My Solution
def detect_cycle(head):
    nodes = []
    curr = head
    while curr:
        if curr in nodes:
            return curr
        nodes.append(curr)
        curr = curr.next
        
    return None

#-------------------------------------------------------------------------------
# CTCI Solution 
def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast

#-------------------------------------------------------------------------------
#Testing

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

class Test(unittest.TestCase):
  def test_detect_cycle(self):
    head1 = Node(100,Node(200,Node(300)))
    self.assertEqual(detect_cycle(head1), None)
    node1 = Node(600)
    node2 = Node(700,Node(800,Node(900,node1)))
    node1.next = node2
    head2 = Node(500,node1)
    self.assertEqual(detect_cycle(head2), node1)

if __name__ == "__main__":
  unittest.main()