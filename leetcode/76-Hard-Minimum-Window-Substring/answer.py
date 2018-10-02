#!/usr/bin/python3

#------------------------------------------------------------------------------
# Optimal O(n)
#------------------------------------------------------------------------------

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # Add all targets to a dictionary
        target_count = collections.defaultdict(int)
        for c in t:
            target_count[c] += 1
        # Keep track of all starting and ending indices
        start, end = 0, len(s)+1
        curr_start = 0
        remaining = len(t)
        
        # For every index to keep track of the ending pos starting at 1
        for curr_end, c in enumerate(s, 1):
            # If char is > 0 then it is a target, and we must decrement remaining
            if target_count[c] > 0:
                remaining -= 1
            # Keep track of every single char, target or not
            target_count[c] -= 1
            
            # If we hit all of our targets...
            if remaining == 0:
                # If there are any nontarget chars at the beginning, delete them!
                while target_count[s[curr_start]] < 0:
                    target_count[s[curr_start]] += 1
                    curr_start += 1
                
                # Compare our current window to our result window
                if curr_end - curr_start < end - start:
                    start, end = curr_start, curr_end
                
                target_count[s[curr_start]] += 1
                curr_start += 1
                remaining += 1
                
        # If target not found return ""
        # Else return our window
        if end > len(s):
            return ""
        return s[start:end]

#------------------------------------------------------------------------------
# Brute Force
#------------------------------------------------------------------------------

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        starting = []
        # Creates list of all possible starts
        for i in range(len(s)):
            if s[i] in t:
                starting.append(i)
                
        result = ""
        for start in starting:
            curr = list(t)
            curr_result = ""
            for i in range(start, len(s)):
                if len(curr) == 0:
                    break
                if s[i] in curr:
                    curr.remove(s[i])
                curr_result += s[i]
            
            if len(curr) == 0 and (len(curr_result) < len(result) or result == ""):
                result = curr_result
        
        return result

#------------------------------------------------------------------------------
