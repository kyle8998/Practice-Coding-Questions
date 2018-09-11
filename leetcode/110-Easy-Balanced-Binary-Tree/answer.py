#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        balance = abs(self.getMaxHeight(root.left)-self.getMaxHeight(root.right))
        if balance > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getMaxHeight(self, root):
        if root is None: return 0
        return 1 + max(self.getMaxHeight(root.left), self.getMaxHeight(root.right))
#-------------------------------------------------------------------------------
