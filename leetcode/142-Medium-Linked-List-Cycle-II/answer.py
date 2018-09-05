#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        l1, l2 = self.split_list(head)
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.merge(l1, l2)
        
    def split_list(self, head):
        """
        Split the list in half
        """
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow.next, slow = None, slow.next
        return (head, slow)
    
    def merge(self, head1, head2):
        """
        Combine the two lists
        """
        dummy = ListNode(None)
        node = dummy
        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next
            
        # Get the remaining nodes if necessary
        node.next = head1 or head2
        return dummy.next
#-------------------------------------------------------------------------------

