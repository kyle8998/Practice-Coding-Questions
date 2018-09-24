#!/usr/bin/python3

#------------------------------------------------------------------------------

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Our products list must have a leading 0 because a product may carry over
        products = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                products[i+j+1] += int(num2[j])*int(num1[i])
                
        # Calculate each digit and each carry
        carry = 0
        for i in range(len(products)-1, -1, -1):
            products[i], carry = (products[i] + carry) % 10, (products[i] + carry) // 10
        
        # Just put the digits in a string!
        result = ""
        for digit in products:
            result += str(digit)
            
        return result.lstrip("0")

#------------------------------------------------------------------------------
#Testing
