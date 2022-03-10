# -*- coding: utf-8 -*-
"""
@author: brand
"""

# Implement a function that converts a fixed<w, b> representation to a real number. 
# Use two's complement for negative numbers. 

# The function signature is 
# def fromFixedPoint(w: int, b:int, bits:[int]) -> float:
#     w: width of the binary representation
#     b: binary point

# Test the following inputs:

# fromFixedPoint(10, 3, [0, 1, 0, 1, 1, 0, 0, 1, 1, 0])
# fromFixedPoint(10, 5, [1, 0, 0, 1, 0, 1, 0, 1, 1, 1])
# fromFixedPoint(8, 2, [1, 0, 1, 0, 1, 0, 1, 1])

def fromFixedPoint(w: int, b:int, bits:[int]) -> float:
    x = -bits[0]*(2**(w-1-b))
    for i in range(1,w):
        a = bits[i] * (2 ** (w - 1 - i - b))
        x += a
    return x

fromFixedPoint(10, 3, [0, 1, 0, 1, 1, 0, 0, 1, 1, 0])
# 44.75

fromFixedPoint(10, 5, [1, 0, 0, 1, 0, 1, 0, 1, 1, 1])
# -13.28125

fromFixedPoint(8, 2, [1, 0, 1, 0, 1, 0, 1, 1])
# -21.25
