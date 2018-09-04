#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#-------------------------------------------------------------------------------
# Iterative Solution

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        stack = [root]
        
        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left

            # Add nodes to the stack
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return root

#-------------------------------------------------------------------------------
# Recursive Solution

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root

#-------------------------------------------------------------------------------
