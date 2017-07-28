#!/usr/bin/python

class Solution(object):
        def lengthOfLongestSubstring(self, s):
            """
            :type s: str
            :rtype: int
            """

            length = 0
            i = 0
            j = 0
            substring = set()
            while i < len(s) and j < len(s):
                if not s[i] in substring:
                    substring.add(s[i])
                    i += 1
                    length = max(length, i - j)
                else:
                    substring.remove(s[j])
                    j += 1
            return length
#-------------------------------------------------------------------------------
# Optimized o(n) solution

class Optimized(object):
        def lengthOfLongestSubstring(self, s):
            length = 0
            i = 0
            j = 0
            dict = {}
            for j in range (0, len(s)):
                if s[j] in dict:
                    i = max(dict[s[j]], i)
                length = max(length, j - i + 1)
                dict[s[j]] = j + 1

            return length

#-------------------------------------------------------------------------------
#Testing

def main():
    x = Optimized()
    y = x.lengthOfLongestSubstring("abcdedfffqwertyuioplkjtksladnf")
    print y

main()
