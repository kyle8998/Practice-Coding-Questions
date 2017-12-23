#!/usr/bin/env python

#-------------------------------------------------------------------------------
# My Solution
#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        unique = []
        
        # Initialize prev and curr - return if 1 or 0 element list
        if head and head.next:
            prev = head
            curr = head.next
            unique.append(prev.val)
        else:
            return head
        
        # Iterate through list adding each unique value to the list
        while curr:
            if curr.val not in unique:
                unique.append(curr.val)
                curr = curr.next
                prev = prev.next
            else:
                curr = curr.next
                prev.next = curr
                
        return head
#-------------------------------------------------------------------------------
# Optimized Solution
#-------------------------------------------------------------------------------
    def deleteDuplicates2(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head
#-------------------------------------------------------------------------------
# Testing
