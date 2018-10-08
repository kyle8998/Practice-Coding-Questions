#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# solution
#-------------------------------------------------------------------------------

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isvalid(s):
            """
            Check to see if the string is valid
            """
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
    
        # Leading ) or trailing ( will always be invalid
        s = s.lstrip(')').rstrip('(')
        
        possible = [s]
        while True:
            # Use our valid function to only filter the valid possiblities
            valid = list(filter(isvalid, possible))
            if valid:
                return valid

            # Determine all possible deletions at this point
            new = set()
            for s in possible:
                for i in range(len(s)):
                    # Remove parenthesis at index i
                    new.add(s[:i] + s[i+1:])
            possible = new

            # List comprehension for the same thing
            # possible = [s[:i] + s[i+1:] for s in possible for i in range(len(s))]

#-------------------------------------------------------------------------------
