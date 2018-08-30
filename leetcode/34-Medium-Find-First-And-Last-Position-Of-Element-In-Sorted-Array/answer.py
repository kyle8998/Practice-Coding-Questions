#!/usr/bin/python3

#------------------------------------------------------------------------------

# This first solution is technically O(log(n)+k) where k is the number of occurances of target
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binarySearch(nums, target, 0, len(nums)-1)
        if left == -1: return [-1, -1]
        right = left
        
        while nums[left] == target and left > 0:
            left -= 1
        if nums[left] != target:
            left += 1
        while nums[right] == target and right < len(nums)-1:
            right += 1
        if nums[right] != target:
            right -= 1
        
        return [left, right]
    
    def binarySearch(self, nums, target, left, right):
        """
        Binary Search for log(n) time
        """
        if right >= left:
            mid = (left + right ) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binarySearch(nums, target, left, mid-1)
            else:
                return self.binarySearch(nums, target, mid+1, right)
        else:
            return -1

#------------------------------------------------------------------------------

# This second solution is O(2log(n))
class Solution:
    def searchRange(self, nums, target):
        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > A[mid]: left = mid + 1
                else: right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]: left = mid + 1
                else: right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]

#------------------------------------------------------------------------------
#Testing
