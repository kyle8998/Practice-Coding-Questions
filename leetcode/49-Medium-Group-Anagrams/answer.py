#!/usr/bin/python3

#------------------------------------------------------------------------------

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strs:
            sort = "".join(sorted(s))
            if sort in groups:
                groups[sort].append(s)
            else:
                groups[sort] = [s]

        return [groups[i] for i in groups.keys()]

#------------------------------------------------------------------------------
#Testing
