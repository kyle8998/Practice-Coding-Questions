# CTCI 4.2
# Minimal Tree

import unittest
import math

class Node:

    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'
        

# My Solution

def minTree(arr):
    #mIdx = len(arr)/2
    #mid = arr[mIdx]
    #left = arr[0:mIdx]
    #right = arr[mIdx+1:len(arr)]
    
    # Rather than pass around entire arrays, try passing the indices
    return helper(arr, 0, len(arr)-1)
    
def helper(arr, left, right):
    if left > right:
        return
    # Find middle of list
    mid = math.floor((left + right) / 2)
    
    # Creates the tree
    root = Node(arr[mid])
    # Recursively call to find left and right trees
    root.left = helper(arr, left, mid - 1)
    root.right = helper(arr, mid + 1, right)
    
    return root
    
    
    

#-------------------------------------------------------------------------------
# CTCI Solution 


#-------------------------------------------------------------------------------
#Testing

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
print(minTree(testArray))