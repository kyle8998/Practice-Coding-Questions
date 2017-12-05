#!/usr/bin/env python

#-------------------------------------------------------------------------------
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # range to -1, because of the uninclusive lower bound
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] > 9:
                # if it is 9, set to zero and repeat on left element
                digits[i] = 0
                # if it is leftmost, insert a 1 in the head
                if i == 0:
                    digits.insert(0, 1)
            # break if add has no complications
            else:
                break;

        return digits
#-------------------------------------------------------------------------------
# Testing
