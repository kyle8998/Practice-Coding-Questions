#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def help(left, right):
            if left > right: return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = help(left, mid-1)
            root.right = help(mid+1, right)
            return root
            
        return help(0, len(nums)-1)

#-------------------------------------------------------------------------------
# Testing
