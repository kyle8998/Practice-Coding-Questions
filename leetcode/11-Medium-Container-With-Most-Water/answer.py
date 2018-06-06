#!/usr/bin/python3

#------------------------------------------------------------------------------

import itertools

class Solution:
    """
    :type height: List[int]
    :rtype: int
    """
    # Two Pointer Approach O(n)
    def maxArea(self, height):
        # Start on outside and move in based on the shorter side
        result, l, r = 0, 0, len(height)-1
        while(l < r):
            if height[l] <= height[r]:
                result = max(result, (r-l)*height[l])
                l += 1
            else:
                result = max(result, (r-l)*height[r])
                r -= 1

        return result

#-------------------------------------------------------------------------------

    # Brute Force O(n^2)
    def maxAreaBrute(self, height):
        # Brute force O(n^2)
        result = 0
        for i1, a1 in enumerate(height):
            for i2, a2 in enumerate(height):
                if i1 == i2: continue
                if a1 <= a2:
                    result = max(result, abs(i2-i1)*a1)

        return result

#------------------------------------------------------------------------------
#Testing

