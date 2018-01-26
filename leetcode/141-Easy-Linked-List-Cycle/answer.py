#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # We know a linkedList has a cycle if and only if it encounters an element again
        if head is not None:
            slow = head
            fast = head
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
                if slow is fast:
                    return True
                
        return False
        
#-------------------------------------------------------------------------------
# Testing
