#!/bin/python3

import sys
from fractions import Fraction

def main():
    pegs = [4, 30, 50, 60]
    # your code here
    length = len(pegs)

    # If the length is odd or even
    if length % 2 == 0: even = True
    else: even = False

    # Set result equal to first peg
    result = pegs[0]
    if even: result -= pegs[length - 1]
    else: result += pegs[length - 1]

    # Done if length = 2
    if length > 2:
        for i in range(1, length - 1):
            # Alternate signs
            result += (-1)**i * 2 * pegs[i]

    if even: result *= (-2/3)
    else: result *= -2

    print(Fraction(result).limit_denominator().numerator)

    print(float(2)/3)

main()
