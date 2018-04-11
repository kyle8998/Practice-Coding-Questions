#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #-------------------------------------------------------------------------------
    # Clean Solution
    #-------------------------------------------------------------------------------
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1
        
    #-------------------------------------------------------------------------------
    # Less optimal/clean solution
    #-------------------------------------------------------------------------------
    def minDepth2(self, root):
        if root:
            return self.help(root, 1)
        return 0
        
    def help(self, root, count):
        if root is None:
            # Probably a bad way to do this lol
            return 99999999
        if root.left is None and root.right is None:
            return count
        return min(self.help(root.left, count+1), self.help(root.right, count+1))
        
#-------------------------------------------------------------------------------
# Testing
