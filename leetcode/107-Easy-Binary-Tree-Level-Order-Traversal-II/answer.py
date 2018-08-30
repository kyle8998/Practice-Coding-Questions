#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Clean iterative solution with list comprehension
class Solution:
    def levelOrderBottom(self, root):
            row = [root]
            ans = []
            while any(row):
                ans.insert(0, [node.val for node in row])
                row = [kid for node in row for kid in (node.left, node.right) if kid]

            return ans

#-------------------------------------------------------------------------------
# Recursive Solution kinda faster than the next, no nonsense
class Solution
    def levelOrderBottom(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            def dfs(root, depth):
                if root:
                    if len(stack) == depth:
                        stack.insert(0, [])
                    stack[-depth - 1].append(root.val)
                    dfs(root.left, depth + 1)
                    dfs(root.right, depth + 1)
            stack = []
            dfs(root, 0)
            return stack

#-------------------------------------------------------------------------------
# Slightly slower solution      
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_list = {}
        result = []
        self.dfs(root, 0, level_list)
        for v in level_list.values():
            result.append(v)
        result.reverse()
        return result
    
    def dfs(self, root, level, level_list):
        """
        Does a dfs to get level of each node
        """
        if not root:
            return
        if level not in level_list:
            level_list[level] = [root.val]
        else:
            level_list[level].append(root.val)
            
        self.dfs(root.left, level+1, level_list)
        self.dfs(root.right, level+1, level_list)

#-------------------------------------------------------------------------------
# Testing
