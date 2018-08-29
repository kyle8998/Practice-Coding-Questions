#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isEqual(root, root)
        
    def isEqual(self, n1, n2):
        if not n1 and not n2: return True
        if not n1 or not n2: return False
        return (n1.val == n2.val) and self.isEqual(n1.right, n2.left) and self.isEqual(n1.left, n2.right)
            
#-------------------------------------------------------------------------------
# Testing
