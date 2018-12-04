#!/usr/bin/env python3

#-------------------------------------------------------------------------------
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(i):
            # If we encounter a node already in the stack
            if visited[i] == -1:
                return False
            # If we encounter a node we already checked previously
            if visited[i] == 1:
                return True
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            return True
        
        # Create adj matrix and visited cache
        graph = [[] for _ in range(numCourses)]
        # 0 = Not visited, -1 = currently in stack, 1 = already visited and is good
        visited = [0 for _ in range(numCourses)]
        
        # Iterate through all edges to populate graph
        for i, j in prerequisites:
            # Course i requires course j, so the edge goes j -> i
            graph[j].append(i)
        
        # Perform dfs on each course
        for i in range(numCourses):
            # If we detect a cycle return false, else true
            if not dfs(i):
                return False
        return True--------------------------------------------------------
# Testing
