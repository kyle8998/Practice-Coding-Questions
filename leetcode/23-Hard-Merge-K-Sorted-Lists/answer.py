#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#-------------------------------------------------------------------------------
# Merge Sort Solution
#-------------------------------------------------------------------------------

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return None
        def mergeTwoLists(node1, node2):
            dummy = ListNode(0)
            cur, cur1, cur2 = dummy, node1, node2
            while cur1 and cur2:
                cur.next = cur1 if cur1.val < cur2.val else cur2
                if cur.next == cur1:
                    cur1 = cur1.next
                else:
                    cur2 = cur2.next
                cur = cur.next
            cur.next = cur1 or cur2
            return [dummy.next]

        def mergelists(Lists):
            if len(Lists) == 1:
                return Lists
            elif len(Lists) == 2:
                return mergeTwoLists(Lists[0], Lists[1])
            else:
                low, high = 0, len(Lists)
                mid = (low+high)//2
                return mergeTwoLists(mergelists(Lists[low:mid])[0], mergelists(Lists[mid:high])[0])

        return mergelists(lists)[0]
#-------------------------------------------------------------------------------
# First Solution (Time Limit Exceeded)
#-------------------------------------------------------------------------------

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        for i in range(len(lists)-1, -1, -1):
                if not lists[i]:
                    lists.pop(i)
        dummy = ListNode(None)
        curr = dummy
        while lists:
            smallest = float('inf')
            idx = 0
            for i in range(len(lists)-1, -1, -1):
                if lists[i] and lists[i].val < smallest:
                    smallest = lists[i].val
                    idx = i
            curr.next = ListNode(smallest)
            curr = curr.next
            lists[idx] = lists[idx].next
            for i in range(len(lists)-1, -1, -1):
                if not lists[i]:
                    lists.pop(i)
        return dummy.next

#-------------------------------------------------------------------------------
