#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Solution
#-------------------------------------------------------------------------------

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        i, j = 0, len(matrix[0])-1
        
        while 0 <= i < len(matrix) and 0 <= j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False

#-------------------------------------------------------------------------------
