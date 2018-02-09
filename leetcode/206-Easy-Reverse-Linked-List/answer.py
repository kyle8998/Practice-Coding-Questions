#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        
        while head:
            head.next, prev, head = prev, head, head.next
            
        return prev
#-------------------------------------------------------------------------------
# Testing
