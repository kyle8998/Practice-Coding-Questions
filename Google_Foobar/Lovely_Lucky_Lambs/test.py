#!/bin/python

import sys

def main():
    # your code here

    print("hi")
    # Must find generous and stingy solution
    # Want to return index to get # of people
    total_lambs = 13
    generous_result = generous(total_lambs, 0, 0)
    stingy_result = stingy(total_lambs, 0, 0, 0)

    print(generous_result)
    print(stingy_result)
    print (stingy_result - generous_result)

# 2*X_n-1 Series
def generous(total_lambs, prev, count):
    # Base Case
    if count >= total_lambs:
        return 0
    elif count > total_lambs:
        return -1
        
    if prev == 0:
        return 1 + generous(total_lambs, 1, 1)
    else:
	 # Special case where you can hire another without breaking the rules
        if count + prev * 2 > total_lambs and (total_lambs - count >= (prev + prev / 2)):
            return 1 + generous(total_lambs, prev * 2, total_lambs)
        return 1 + generous(total_lambs, prev * 2, count + prev * 2)
    
# Fibonacci Series
def stingy(total_lambs, prev1, prev2, count):
    # Base Case
    if count == total_lambs:
        return 0
    elif count > total_lambs:
        return -1
        
    if prev1 == 0 and prev2 == 0:
        return 1 + stingy(total_lambs, 1, 0, 1)
    elif prev2 == 0:
        return 1 + stingy(total_lambs, 1, 1, 2)
    else:
        return 1 + stingy(total_lambs, prev1 + prev2, prev1, count + prev1 + prev2)


main()
