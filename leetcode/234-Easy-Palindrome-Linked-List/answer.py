#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#-------------------------------------------------------------------------------
# O(n) Time, O(1) Space Complexity (Slightly slower than O(n) space solution)
#-------------------------------------------------------------------------------

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Use fast slow runner to find midpoint
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        # Reverse the second half of the list
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
            
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

#-------------------------------------------------------------------------------
# Simple Solution with O(n) Space Complexity
#-------------------------------------------------------------------------------


class Solution:
    def isPalindrome(self, head):
        curr = head
        elements = []
        while curr:
            elements.append(curr.val)
            curr = curr.next
            
        return elements == elements[::-1]
#-------------------------------------------------------------------------------
