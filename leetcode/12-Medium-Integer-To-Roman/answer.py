#!/usr/bin/python

#------------------------------------------------------------------------------

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        # Create lists of possible roman numerals
        M = ["", "M", "MM", "MMM"];
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        
        # Perform calculations and append to result
        result += M[num / 1000]
        result += C[(num % 1000) / 100]
        result += X[(num % 100) / 10]
        result += I[num % 10]
        
        return result

#------------------------------------------------------------------------------
#Testing

def main():
    print Solution().intToRoman(3114)




main()
