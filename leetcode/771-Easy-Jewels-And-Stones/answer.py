#!/usr/bin/env python3

#-------------------------------------------------------------------------------
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([i in J for i in S])
#-------------------------------------------------------------------------------
