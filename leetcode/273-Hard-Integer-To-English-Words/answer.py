#!/usr/bin/env python3

#-------------------------------------------------------------------------------
# solution
#-------------------------------------------------------------------------------

class Solution:
    lessThan20 = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven",
                           "Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    thousands = ["","Thousand","Million","Billion"]
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 20:
            return self.lessThan20[num]
        
        res = ""
        # Loop for length of thousands places (max groups of 3 digits)
        for i in range(len(self.thousands)):
            # extract the last three digits
            right = num % 1000
            if right != 0:
                res = self.getWords(right) + self.thousands[i] + " " + res
            # Remove the last three digits
            num //= 1000
        return res.strip()
        
        
    def getWords(self, num):
        """
        This function will convert any 1-3 digit number to words
        """
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            # Extract tens digit then recursively get rightmost digit
            return self.tens[num//10] + " " + self.getWords(num%10)
        else:
            # Extract hundreds digit, append "Hundred" then recurse on right two digits
            return self.lessThan20[num//100] + " Hundred " + self.getWords(num%100)

#-------------------------------------------------------------------------------
