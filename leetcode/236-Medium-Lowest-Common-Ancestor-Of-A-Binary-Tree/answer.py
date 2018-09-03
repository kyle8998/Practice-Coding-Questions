#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#-------------------------------------------------------------------------------
# My brute force solution

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val == p.val or root.val == q.val:
            return root
        if self.search(root.left, p.val) and self.search(root.left, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.search(root.right, p.val) and self.search(root.right, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
    
    def search(self, root, target):
        if not root: return False
        if root.val == target: return True
        return self.search(root.left, target) or self.search(root.right, target)


#-------------------------------------------------------------------------------
# Optimal Solution

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root
        left = right = None
        
        # Do DFS
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
            
        # If found on both sides, the current node is the ancestor
        if left and right:
            return root
        else:
            # This will return the nonnone node
            return left or right
#-------------------------------------------------------------------------------
