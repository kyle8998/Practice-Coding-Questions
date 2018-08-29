#!/usr/bin/python3

#------------------------------------------------------------------------------
# First Solution
#------------------------------------------------------------------------------

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        water = 0
        water_differences1 = [0]*len(height)
        trapped1 = []
        curr = 0
        beg = 0
        # Go left to right
        for i in range(len(height)):
            if height[i] >= curr:
                curr = height[i]
                if i - beg > 1:
                    trapped1.append((beg, i))
                beg = i
            else:
                water_differences1[i] = (curr - height[i])
        
        curr = 0
        water_differences2 = [0]*len(height)
        trapped2 = []
        end = len(height)-1
        # Go right to left
        for i in range(len(height)-1, -1, -1):
            if height[i] >= curr:
                curr = height[i]
                if end - i > 1:
                    trapped2.append((i, end))
                end = i
            else:
                water_differences2[i] = (curr - height[i])
        
        # Combine lists and get rid of dupes
        trapped = list(set(trapped1).union(set(trapped2)))
        
        # Go through the guarenteed trapped water list and get the right amount
        for i, j in trapped:
            for k in range(i+1, j):
                water += min(water_differences1[k], water_differences2[k])

        return water
        
#------------------------------------------------------------------------------
# Second Solution
#------------------------------------------------------------------------------
        
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        r, redge = len(height) - 1, len(height) - 1
        l, ledge = 0, 0
        ans = 0

        # Go from left and right until they meet
        while l < r:
            if height[l] <= height[r]:
                l += 1
                if height[l] < height[ledge]:
                    ans += height[ledge] - height[l]
                else:
                    ledge = l
            else:
                r -= 1
                if height[r] < height[redge]:
                    ans += height[redge] - height[r]
                else:
                    redge = r
        return ans

#------------------------------------------------------------------------------
#Testing
