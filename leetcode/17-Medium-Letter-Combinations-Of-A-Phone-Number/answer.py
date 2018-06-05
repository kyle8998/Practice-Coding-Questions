#!/usr/bin/python

#------------------------------------------------------------------------------

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        return self.helper("", digits, [])
        
    def helper(self, prefix, digits, result):
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if len(digits) == 0:
            result.append(prefix)
            return result
        chars = mapping[int(digits[0])]
        for c in chars:
            self.helper(prefix+c, digits[1:], result)
        return result

#------------------------------------------------------------------------------
#Testing

