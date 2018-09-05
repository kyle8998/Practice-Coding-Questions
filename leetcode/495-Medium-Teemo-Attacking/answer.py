#!/usr/bin/env python3

#-------------------------------------------------------------------------------

class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 0:
            return 0
        elif len(timeSeries) == 1:
            return duration
        
        time = 0
        # Loop through each attack and add the appropriate duration
        for i in range(len(timeSeries)-1):
            diff = timeSeries[i+1] - timeSeries[i]
            if diff < duration:
                time += diff
            else:
                time += duration

        # Add last attack
        time += duration
        
        return time

#-------------------------------------------------------------------------------
