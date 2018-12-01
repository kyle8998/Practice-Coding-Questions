#!/usr/bin/python3

#------------------------------------------------------------------------------
# Solution O(n) Stack Solution
#------------------------------------------------------------------------------

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        result = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h * w)
            stack.append(i)
        return result

#------------------------------------------------------------------------------
# Solution O(n) Kinda DP Solution
#------------------------------------------------------------------------------

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        
        # Left and right will be a cache to hold the number of bars to left and right >= curr height
        left = [1 for _ in range(len(heights))]
        right = [1 for _ in range(len(heights))]
        
        # Calculate left
        for i in range(len(heights)):
            l = i-1
            # Grow as far left as possible
            # We make jumps based on the previously computed left values
            while l >= 0:
                if heights[l] >= heights[i]:
                    left[i] += left[l]
                    l -= left[l]
                else:
                    break
        
        # Calculate right
        for i in range(len(heights)):
            r = i+1
            # Grow as far right as possible
            # We make jumps based on the previously computed right values
            while r < len(heights):
                if heights[r] >= heights[i]:
                    right[i] += right[r]
                    r += right[r]
                else:
                    break
            
        # Now we can iterate through all of our possible rectangles
        # We calculate our areas with our height * width (left+right)
        for i in range(len(heights)):
            result = max(result, heights[i] * (left[i] + right[i] - 1))
            
        return result           
        
#------------------------------------------------------------------------------
# Brute Force Solution (O(n^2))
#------------------------------------------------------------------------------

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        # Find the max area for each bar i
        for i in range(len(heights)):
            area = heights[i]
            l, r = i-1, i+1
            
            # Grow as far left as possible
            while l >= 0:
                if heights[l] >= heights[i]:
                    area += heights[i]
                    l -= 1
                else:
                    break
            
            # Grow as far right as possible
            while r < len(heights):
                if heights[r] >= heights[i]:
                    area += heights[i]
                    r += 1
                else:
                    break
            
            result = max(result, area)
            
        return result
            

#------------------------------------------------------------------------------
