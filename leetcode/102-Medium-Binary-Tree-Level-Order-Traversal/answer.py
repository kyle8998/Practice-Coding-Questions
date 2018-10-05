#!/usr/bin/python3

#------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = [(root, 0)]
        result = []
        
        while stack:
            (node, level) = stack.pop(0)
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            if node.left: stack.append((node.left, level+1))
            if node.right: stack.append((node.right, level+1))
            
        return result 

#------------------------------------------------------------------------------
#Testing
