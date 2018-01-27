#!/usr/bin/python

#------------------------------------------------------------------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head:
            fast = head
            slow = head
        
            for _ in range(n):
                if fast:
                    fast = fast.next
                else:
                    return None
                
            # head case
            if not fast:
                head = head.next
                return head
                
            # This will bring slow up to the correct node
            while fast.next:
                fast = fast.next
                slow = slow.next
                
            # Remove the node after slow
            slow.next = slow.next.next
            return head
                
#------------------------------------------------------------------------------
#Testing
