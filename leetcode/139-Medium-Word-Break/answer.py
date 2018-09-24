#!/usr/bin/env python3

#-------------------------------------------------------------------------------
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Cache booleans for places in the string that matches a word
        # Put a True at beginning to signify start
        dp = [True] + [False]*len(s)
        for i in range(len(s)):
            for word in wordDict:
                # If current substring matches word and last word was valid then set True
                if word == s[i-len(word)+1:i+1] and dp[i-len(word)+1]:
                    dp[i+1] = True
        return dp[-1]
        
#-------------------------------------------------------------------------------
# Testing
