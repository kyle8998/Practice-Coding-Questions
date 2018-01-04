# CTCI 2.6
# Palindrome

import unittest
#from LinkedList import LinkedList

# My Solution
    
# Simple solution abusing python's list functionality
def is_palindrome1(head):
    curr = head
    list = []
    
    # This adds everything in the linked list to a list
    while curr:
        list.append(curr.data)
        curr = curr.next
        
    # Checks list with the reverse of itself
    # ::-1 creates a shallow copy of the list where it indexes in reverse
    if list == list[::-1]:
        return True
    else:
        return False

# Second solution using the list as a stack        
def is_palindrome(head):
    slow = fast = head
    list = []

    while fast and fast.next:
        list.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # If it is odd, skip the middle element
    if fast:
        slow = slow.next

    # Compare rest of slow runner to popped stack
    while slow:
        if slow.data != list.pop():
            return False
        slow = slow.next

    return True


#-------------------------------------------------------------------------------
# CTCI Solution

def ais_palindrome(ll):
    fast = slow = ll.head
    stack = []

    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True


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
  def test_palindrome(self):
    list1 = Node(10)
    self.assertTrue(is_palindrome(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(is_palindrome(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(is_palindrome(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(is_palindrome(list4))
    
''''
  def test_copy_reverse(self):
    head = Node(10,Node(20,Node(30,Node(40))))
    self.assertEqual(str(copy_reverse(head)), "40,30,20,10")
'''

if __name__ == "__main__":
  unittest.main()