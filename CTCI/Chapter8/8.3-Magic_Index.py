# CTCI 8.3
# Magic Index

import math

#-------------------------------------------------------------------------------
# My Solution
#-------------------------------------------------------------------------------
# BRUTE FORCE O(n)
#-------------------------------------------------------------------------------
def magic_index_brute(arr):
    if arr:
        for idx, n in enumerate(arr):
            if idx == n:
                return idx
    return -1
#-------------------------------------------------------------------------------
# SOLUTION FOR DISTINCT SORTED LISTS ... O(log(n))
#-------------------------------------------------------------------------------
def magic_index_distinct(arr):
    if arr is None:
        return -1
    return helper(arr, 0, len(arr)-1)
    
def helper(arr, min, max):
    # If it ever gets out of the bounds (min > max)
    if min > max:
        return -1
    # Calculate the midpoint
    mid = math.floor((min + max)/2)
    # If it is the magic index return it
    if mid == arr[mid]:
        return mid
    # If the element is less recurse on the right list
    if arr[mid] < mid:
        return helper(arr, mid+1, max)
    # If the element is more recurse on the left list
    if arr[mid] > mid:
        return helper(arr, min, mid-1)     
#-------------------------------------------------------------------------------
# SOLUTION FOR ANY SORTED LISTS ... O(log(n))
#-------------------------------------------------------------------------------    
def magic_index(arr):
    if arr is None:
        return -1
    return helper2(arr, 0, len(arr)-1)
    
def helper2(arr, start, end):
    # If it ever gets out of the bounds (min > max)
    if start > end:
        return -1
    # Calculate the midpoint
    mid = math.floor((start + end)/2)
    mid_value = arr[mid]
    # If it is the magic index return it
    if mid == mid_value:
        return mid

    # Search left side
    left = min(mid-1, mid_value)
    left_value = helper2(arr, start, left)
    if left_value >= 0:
        return left_value

    # Search right side
    right = max(mid+1, mid_value)
    right_value = helper2(arr, right, end)
    if right_value >= 0:
        return right_value
        
    return -1

#-------------------------------------------------------------------------------
#Testing
#-------------------------------------------------------------------------------

import unittest

class Test(unittest.TestCase):
  def test_magic_index_distinct(self):
    self.assertEqual(magic_index_distinct([3,4,5]), -1)
    self.assertEqual(magic_index_distinct([-2,-1,0,2]), -1)
    self.assertEqual(magic_index_distinct([-20,0,1,2,3,4,5,6,20]), -1)
    self.assertEqual(magic_index_distinct([-20,0,1,2,3,4,5,7,20]), 7)
    self.assertEqual(magic_index_distinct([-20,0,1,2,4,6,7,20]), 4)
  
  def test_magic_index(self):
    self.assertEqual(magic_index([3,4,5]), -1)
    self.assertEqual(magic_index([-2,-1,0,2]), -1)
    self.assertEqual(magic_index([-20,0,1,2,3,4,5,6,20]), -1)
    self.assertEqual(magic_index([-20,0,1,2,3,4,5,7,20]), 7)
    self.assertEqual(magic_index([-20,1,3,4,5,6,7,20]), 1)
    self.assertEqual(magic_index([-20,5,5,5,5,5,6,20]), 6)

if __name__ == "__main__":
  unittest.main()