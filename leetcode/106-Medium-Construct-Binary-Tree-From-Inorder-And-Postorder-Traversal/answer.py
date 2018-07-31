#!/usr/bin/python3

#------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        if len(postorder) == 0 or len(inorder) == 0:
            return None
        
        tree = TreeNode(postorder[-1])
        j = inorder.index(postorder[-1])
        
        tree.right = self.buildTree(inorder[j+1:], postorder[j:-1])
        tree.left = self.buildTree(inorder[:j], postorder[:j])
        
        return tree  

#------------------------------------------------------------------------------
#Testing
