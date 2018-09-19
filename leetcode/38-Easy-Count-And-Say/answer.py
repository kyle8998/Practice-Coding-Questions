#!/usr/bin/env python3

#-------------------------------------------------------------------------------

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        # Iterate n times
        while n > 1:
            count, prev, new = 1, 0, ""
            # Loop though until number changes to count occurances
            for i in range(1, len(result)):
                if result[i] == result[prev]:
                    count += 1
                else:
                    new += str(count)+str(result[prev])
                    count, prev = 1, i
            # Add the last count and decrement n
            result = new + str(count) + str(result[prev])
            n -= 1
        return result
        
#-------------------------------------------------------------------------------
