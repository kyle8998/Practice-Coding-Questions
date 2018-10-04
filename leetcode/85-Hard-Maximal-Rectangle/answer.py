#!/usr/bin/python3

#------------------------------------------------------------------------------
# Solution
#------------------------------------------------------------------------------

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        # Keep track of all heights
        height = [0] * (len(matrix[0])+1)
        result = 0
        
        for row in range(len(matrix)):
            
            # This will calculate the heights growing downwards
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    height[col] = height[col] + 1
                else:
                    height[col] = 0
                    
            # Calculate the area for that row of heights
            # Have -1 in to default to the last element of heights array which will be 0
            stack = [-1]
            for i in range(len(matrix[0])+1):
                # While the current height is less than the previous heights
                # This will find the longest rectangle of that height
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    result = max(result, h * w)
                # Move to next
                stack.append(i)
            
        return result               
        
#------------------------------------------------------------------------------
# My First Solution (May not work in every case)
#------------------------------------------------------------------------------

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def grow(top, bot, left, right):
            if top < 0 or bot > len(matrix) or left < 0 or right > len(matrix[0]):
                return 0
            result = [(right-left+1)*(bot-top+1)]
            if check_row(top-1, left, right):
                up = grow(top-1, bot, left, right)
                result.append(up)
            if check_row(bot+1, left, right):
                down = grow(top, bot+1, left, right)
                result.append(down)
            if check_col(left-1, top, bot):
                left = grow(top, bot, left-1, right)
                result.append(left)
            if check_col(right+1, top, bot):
                right = grow(top, bot, left, right+1)
                result.append(right)
            return max(result)
            
        def check_row(row, left, right):
            if 0 <= row < len(matrix):
                for i in range(left, right+1):
                    if matrix[row][i] == '0':
                        return False
                return True
            return False
        
        def check_col(col, top, bot):
            if 0 <= col < len(matrix[0]):
                for i in range(top, bot+1):
                    if matrix[i][col] == '0':
                        return False
                return True
            return False
        
        result = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == '1':
                    area = grow(row, row, col, col)
                    if area > result:
                        result = area
        return result

#------------------------------------------------------------------------------
#Testing
