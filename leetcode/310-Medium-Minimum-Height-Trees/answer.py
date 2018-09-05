#!/usr/bin/env python	
 #-------------------------------------------------------------------------------	
# Accepted Solution	
#-------------------------------------------------------------------------------	
class Solution:	
    def findMinHeightTrees(self, n, edges):	
        """	
        :type n: int	
        :type edges: List[List[int]]	
        :rtype: List[int]	
        """	
        if n == 1: return [0] 	
        	
        # Create adj list using set with both incoming/outgoing	
        adj = [set() for _ in range(n)]	
        for i, j in edges:	
            adj[i].add(j)	
            adj[j].add(i)	
         # Get Leaves	
        leaves = [i for i in range(n) if len(adj[i]) == 1]	
         # Loop and take off leaves until left with middle	
        while n > 2:	
            n -= len(leaves)	
            newLeaves = []	
            for i in leaves:	
                j = adj[i].pop()	
                adj[j].remove(i)	
                if len(adj[j]) == 1: newLeaves.append(j)	
            leaves = newLeaves	
        return leaves	
#-------------------------------------------------------------------------------	
 #-------------------------------------------------------------------------------	
# Brute Force Solution	
#-------------------------------------------------------------------------------	
class Solution:	
    # Helper to find height for each node	
    def findHeight(self, adj_list, node, h, visited):	
        if node not in adj_list:	
            return h	
        else:	
            height = h	
            # Recursively find height through all children	
            for n in adj_list[node]:	
                if n not in visited:	
                    # Add to visited, and find height	
                    visited.append(n)	
                    height = max(height, self.findHeight(adj_list, n, h+1, visited))	
                    	
                # If already visited, do not make recursive call	
                else:	
                    height = max(height, h)	
                    	
            return height	
        	
    # BRUTE FORCE	
    # TIME LIMIT EXCEEDED	
    def findMinHeightTrees(self, n, edges):	
        """	
        :type n: int	
        :type edges: List[List[int]]	
        :rtype: List[int]	
        """	
        min_height = -1	
        result = []	
        	
        # Base case?	
        if len(edges) == 0:	
            return [0]	
         # Change into adjacency list for easy use	
        adj_list = {}	
        for e in edges:	
            # Store outgoing edges	
            if e[0] not in adj_list:	
                adj_list[e[0]] = [e[1]]	
            else:	
                adj_list[e[0]].append(e[1])	
                	
            # Also store the incoming edges	
            if e[1] not in adj_list:	
                adj_list[e[1]] = [e[0]]	
            else:	
                adj_list[e[1]].append(e[0])	
         # Perform BFS on each node	
        for n in adj_list:	
            node_height = self.findHeight(adj_list, n, 0, [n])	
            # If node has an equal height, append	
            if min_height == node_height:	
                result.append(n)	
            # If first node or new min is found	
            # Set new min height	
            elif min_height == -1 or min_height > node_height:	
                min_height = node_height	
                result = [n]	
                          	
        return result	
#-------------------------------------------------------------------------------