#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Solution
#-------------------------------------------------------------------------------
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        copy = UndirectedGraphNode(node.label)
        visited = {node: copy}
        stack = [node]
        
        while stack:
            curr = stack.pop()
            for n in curr.neighbors:
                if n not in visited:
                    n_copy = UndirectedGraphNode(n.label)
                    visited[n] = n_copy
                    visited[curr].neighbors.append(n_copy)
                    stack.append(n)
                else:
                    visited[curr].neighbors.append(visited[n])

        return copy

#-------------------------------------------------------------------------------

