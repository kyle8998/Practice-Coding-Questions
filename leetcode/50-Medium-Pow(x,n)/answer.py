#!/usr/bin/python3

#------------------------------------------------------------------------------

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            # Base case, when exponent hits 0 just return 1
            return 1.0
        elif n < 0:
            return 1/self.myPow(x, -n)
        elif n%2:
            # IF ODD
            return self.myPow(x*x,n//2)*x
        else:
            # IF EVEN
            return self.myPow(x*x,n/2)

#------------------------------------------------------------------------------
#Testing
