#!/usr/bin/python

#------------------------------------------------------------------------------
# Time:  O(log(max(m, n)) * log(max_val - min_val))
# Space: O(1)
# Generic solution.
# I did not write this one
class Solution_Generic(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth([nums1, nums2], (len1 + len2)/2 + 1)
        else:
            return (self.getKth([nums1, nums2], (len1 + len2)/2) + \
                    self.getKth([nums1, nums2], (len1 + len2)/2 + 1)) * 0.5

    def getKth(self, arrays, k):
        def binary_search(array, left, right, target, compare):
            while left <= right:
                mid = left + (right - left) / 2
                if compare(array, mid, target):
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def match(arrays, num, target):
            res = 0
            for array in arrays:
                if array:
                    res += len(array) - binary_search(array, 0, len(array) - 1, num, \
                                                    lambda array, x, y: array[x] > y)
            return res < target

        left, right = float("inf"), float("-inf")
        for array in arrays:
            if array:
                left = min(left, array[0])
                right = max(right, array[-1])

        return binary_search(arrays, left, right, k, match)

# Another failure :(
#------------------------------------------------------------------------------

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        # If odd
        if (length1 + length2) % 2 == 1:
            return self.getMed(nums1, nums2, (length1 + length2)/2 + 1)
        else:
            return (self.getMed(nums1, nums2, (length1 + length2)/2 + \
                    self.getMed(nums1, nums2, (length1 + length2)/2 + 1)) * 0.5)

    def getMed(self, A, B, k):
        m = len(A)
        n = len(B)
        if m > n:
            return self.getMed(B, A, k)

        left = 0
        right = m
        while left < right:
            mid = left + ((right - left) / 2)
            if 0 <= k - 1 - mid < n and A[mid] >= B[k - 1 - mid]:
                right = mid
            else:
                left = mid + 1

        AResult = A[left - 1] if left - 1 >= 0 else float("-inf")
        BResult = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")

        return max(AResult, BResult);

# This solution is one big failure
#------------------------------------------------------------------------------
class Failure(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        length1 = len(nums1)
        length2 = len(nums2)
        totalLength = length1 + length2
        i = 1
        idx1 = 0
        idx2 = 0
        odd = False
        if totalLength % 2 == 1:
            totalLength += 1
            odd = True
        half = totalLength / 2

        one = False
        two = False

        while i < half:
            if idx1 == length1:
                two = True
                idx2 += 1
            elif idx2 == length2:
                one = True
                idx1 += 1
            else:
                if nums1[idx1] < nums2[idx2]:
                    idx1 += 1
                else:
                    idx2 += 1
            i += 1
        if idx1 == length1:
            idx1 -= 1
        elif idx2 == length2:
            iidx2 -= 1

        if one:
            result = nums1[idx1]
        elif two:
            result = nums2[idx2]
        else:
            result = float(min(nums1[idx1], nums2[idx2]))

        one = False
        two = False

        if not odd:
            for j in range (0, 1):
                if nums1[idx1] < nums2[idx2]:
                    idx1 += 1
                    if idx1 == length1:
                        two = True
                        break
                else:
                    idx2 += 1
                    if idx2 == length2:
                        one = True
                        break
            if one:
                result = (result + float(nums1[idx1]))/2
            elif two:
                result = (result + float(nums2[idx2]))/2
            else:
                result = (result + min(nums1[idx1], nums2[idx2]))/2

        return result
#------------------------------------------------------------------------------
#Testing

def main():
   # x = Solution()
   # y = x.findMedianSortedArrays([1, 2], [3, 4])
   # print y
   # y = x.findMedianSortedArrays([1, 3], [2])
   # print y
   # y = x.findMedianSortedArrays([1, 2, 5], [3, 6, 7])
   # print y
   # y = x.findMedianSortedArrays([1], [3, 6, 7])
   # print y
   print Solution_Generic().findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6])

main()
