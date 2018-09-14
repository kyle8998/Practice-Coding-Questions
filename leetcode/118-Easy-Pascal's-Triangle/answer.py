#!/usr/bin/env python3

#-------------------------------------------------------------------------------
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        
        triangle = [[1]]
        if numRows == 1:
            return triangle
        
        triangle.append([1,1])
        if numRows == 2:
            return triangle
        
        return self.calculate(triangle, numRows)
        
    def calculate(self, triangle, numRows):
        if len(triangle) == numRows:
            return triangle
        
        curr = len(triangle)
        row = [1]
        for i in range(1, len(triangle[curr-1])):
            row.append(triangle[curr-1][i-1] + triangle[curr-1][i])
        row.append(1)
        triangle.append(row)
        return self.calculate(triangle, numRows)
#-------------------------------------------------------------------------------
