#!/usr/bin/python
from itertools import permutations

#------------------------------------------------------------------------------
# Brute Force Solution
class Solution(object):

    def threeSuma(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        length = len(nums)
        nums.sort()
        for i in xrange(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = length - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k += 1

        return result

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
                if i > 0 and nums[i] == nums[i-1]:
                        continue
                l, r = i+1, len(nums)-1
                while l < r:
                        s = nums[i] + nums[l] + nums[r]
                        if s < 0:
                                l +=1
                        elif s > 0:
                                r -= 1
                        else:
                                res.append((nums[i], nums[l], nums[r]))
                                while l < r and nums[l] == nums[l+1]:
                                        l += 1
                                while l < r and nums[r] == nums[r-1]:
                                        r -= 1
                                l += 1; r -= 1
        return res



    def threeSumBrute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        """
        for i in nums:
            for j in nums:
                if j == i:
                    continue
                for k in nums:
                    if k == j or k == i:
                        continue
                    if (i + j + k) == 0:
                        result.append([i, j, k])
        """
        length = len(nums)

        for i in range(length):
            for j in range(length):
                if j <= i:
                    continue
                for k in range (length):
                    if k <= j or k <= i:
                        continue
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        sum = ([nums[i], nums[j], nums[k]])
                        # Check if there is a permutation inside already
                        inside = False
                        for per in list(permutations(sum, 3)):
                            if per in result:
                                print "hello"
                                inside = True
                                break
                        if not inside:
                            result.append(sum)
        return result

#------------------------------------------------------------------------------
#Testing

def main():
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])




main()
