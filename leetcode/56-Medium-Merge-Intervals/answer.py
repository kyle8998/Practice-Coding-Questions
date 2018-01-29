#!/usr/bin/python

#------------------------------------------------------------------------------

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        intervals.sort(key=lambda x: x.start)
        
        for i in intervals:
            # If list is empty or does not overlap
            if not result or result[-1].end < i.start:
                result.append(i)
                
            # If there is overlap
            else:
                # Change the end of the interval to the higher value
                result[-1].end = max(result[-1].end, i.end)
                
        return result

#------------------------------------------------------------------------------
#Testing
