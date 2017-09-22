#!/usr/bin/python

#------------------------------------------------------------------------------

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(n, str, left, right, arr):
            if len(str) == n*2:
                arr.append(str)
                return
            
            if left < n:
                generate(n, str+"(", left+1, right, arr)
                
            if right < left:
                generate(n, str+")", left, right+1, arr)
        
        arr = []
        generate(n, "", 0, 0, arr)
        return arr

#------------------------------------------------------------------------------
#Testing

def main():
    print Solution().generateParenthesis(4)




main()
