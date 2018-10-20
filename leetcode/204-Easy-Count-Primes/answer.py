#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# Optimal
#-------------------------------------------------------------------------------

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # Check all multiples of number and make sure they are false
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

#-------------------------------------------------------------------------------
# First Solution
#-------------------------------------------------------------------------------

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        
        count = 1
        for i in range(3, n):
            # If i has any factors break, else increment count 
            for j in range(2, int(i**.5)+1):
                if i % j == 0:
                    break
            else:
                print(i)
                count += 1
        
        return count
        
#-------------------------------------------------------------------------------
