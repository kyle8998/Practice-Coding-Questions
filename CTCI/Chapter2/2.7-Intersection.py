# CTCI 2.5
# Sum Lists

import unittest
#from LinkedList import LinkedList

# My Solution
def intersection(head1, head2):
    curr1, curr2 = head1, head2
    len1 = len2 = 1
    diff = 0
    
    # Null Checks
    if not curr1 or not curr2:
        return None

    # Determine if there is an intersection
    # Loop to end of each list and compare
    while curr1 and curr1.next:
        curr1 = curr1.next
        len1 += 1
        
    while curr2 and curr2.next:
        curr2 = curr2.next
        len2 += 1
        
    # If curr1 = curr2 then it intersected
    if curr1 is curr2:
        # Reset currs
        curr1, curr2 = head1, head2
        # Account for different lenth lists
        # Simply take the difference in length and move the proper pointer forward that amount
        if len1 > len2:
            diff = len1 - len2
            for i in range(diff):
                curr1 = curr1.next
                
        elif len2 > len1:
            diff = len2 - len1
            for i in range(diff):
                curr2 = curr2.next
        # Compare each element in both lists until there is a commonality
        while curr1:
            if curr1 is curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next
    # If there is no intersection
    return None

#-------------------------------------------------------------------------------
# CTCI Solution

def aintersection(list1, list2):
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for i in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node

#-------------------------------------------------------------------------------
#Testing

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_intersection(self):
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    self.assertEqual(intersection(head1, head2), None)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    self.assertEqual(intersection(head3, head4), node)

if __name__ == "__main__":
  unittest.main()