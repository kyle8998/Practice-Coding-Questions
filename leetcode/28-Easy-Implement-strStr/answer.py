#!/usr/bin/python

#------------------------------------------------------------------------------
# Python already implements this?
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

#------------------------------------------------------------------------------
#Testing

def main():
    print Solution().strStr("String", "ring")

main()
