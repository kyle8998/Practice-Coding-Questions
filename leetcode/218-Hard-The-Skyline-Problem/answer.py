#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Solution
# Find critical points, store in a max heap using min heap properties (-height)
#-------------------------------------------------------------------------------

import heapq
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        def addsky(pos, hei):
            if sky[-1][1] != hei:
                sky.append([pos, hei])

        sky = [[-1,0]]

        # possible corner positions
        position = set([b[0] for b in buildings] + [b[1] for b in buildings])

        # live buildings
        live = []

        i = 0

        for t in sorted(position):

            # add the new buildings whose left side is lefter than position t
            while i < len(buildings) and buildings[i][0] <= t:
                heapq.heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1

            # remove the past buildings whose right side is lefter than position t
            while live and live[0][1] <= t:
                heapq.heappop(live)

            # pick the highest existing building at this moment
            h = -live[0][0] if live else 0
            addsky(t, h)

        return sky[1:]

#-------------------------------------------------------------------------------
# This does not pass test cases (Memory inefficient)
#-------------------------------------------------------------------------------

class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        if len(buildings) == 1:
            l, r, h = buildings.pop()
            return [[l, h],[r, 0]]
        # Find the right most point
        far_right = 0
        for (_,r,_) in buildings:
            far_right = max(far_right, r)
            
        # Build a 1 dimension height map to track heights
        height_map = [0]*(far_right+1)
        for (l,r,h) in buildings:
            for i in range(l, r):
                if h > height_map[i]:
                    height_map[i] = h
        
        height = 0
        skyline = []
        for i in range(len(height_map)):
            if height_map[i] != height:
                height = height_map[i]
                skyline.append([i, height])
                
        
        return skyline 

#-------------------------------------------------------------------------------
# Testing
