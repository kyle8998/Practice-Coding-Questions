#!/usr/bin/python3

#------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if len(preorder) == 0:
            return None
        
        # Set root to first in preorder
        tree = TreeNode(preorder[0])
        # Find index of that element in inorder
        j = inorder.index(preorder[0])
        
        # Left tree consists of nodes until inorder = preorder
        # Right tree consists of the other half
        tree.left = self.buildTree(preorder[1:j+1], inorder[0:j])
        tree.right = self.buildTree(preorder[j+1:], inorder[j+1:])
        
        return tree   

#------------------------------------------------------------------------------
#Testing
