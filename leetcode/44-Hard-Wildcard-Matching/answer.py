#!/usr/bin/python3

#------------------------------------------------------------------------------
# First Solution
# Not too efficient with all the recursion lol
#------------------------------------------------------------------------------

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        for j in range(len(p)):
            # If str is longer than pattern -> false
            if i > len(s)-1:
                 # it could potentially be true if the remaining characters are *s
                if p[j:].replace("*","") == "":
                    return True
                return False
            if p[j] == '?':
                # If ?, then increment index
                i += 1
            elif p[j] == '*':
                # If last char in pattern, then true
                if j == len(p)-1:
                    return True
                # We want to check all possibilities
                for curr in range(i, len(s)):
                    # If the current char is equal to the next char in the pattern or ?
                    if s[curr] == p[j+1] or p[j+1] == '?' or p[j+1] == '*':
                        if self.isMatch(s[curr:], p[j+1:]):
                            return True
                return False
            else:
                # If any char, check char and increment
                if p[j] != s[i]:
                    return False
                i += 1
        return i == len(s)
                    
                    
        
#------------------------------------------------------------------------------
# DP Solution
#------------------------------------------------------------------------------
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)
        dp = [[False]*(len(p)+1) for i in range(len(s)+1)]
        
        dp[0][0] = True
        
        for i in range(1,len(p)+1):
            if p[i-1] == '*' and dp[0][i-1]:
                dp[0][i] = True
        
        for row in range(1, len(s)+1):
            for col in range(1, len(p)+1):
                if s[row-1] == p[col-1] or p[col-1]=='?':
                    dp[row][col] = True and dp[row-1][col-1]
                elif p[col-1] == '*':
                    dp[row][col] = dp[row][col-1] or dp[row-1][col-1] or dp[row-1][col]
        return dp[len(s)][len(p)]

#------------------------------------------------------------------------------
#Testing
