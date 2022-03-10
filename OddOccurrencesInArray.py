# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 02:05:46 2022

@author: brand
"""

# Find value that occurs in odd number of elements.

# Write a function:
# 	def solution(A)
# that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
# For example, given array A such that:

#  A[0] = 9  A[1] = 3  A[2] = 9
#  A[3] = 3  A[4] = 9  A[5] = 7
#  A[6] = 9
# the function should return 7, as explained in the example above.

# Write an efficient algorithm for the following assumptions:

# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.



def solution(A):
	soln = 0 
	for i in A:
		soln ^= i
	return soln 

#test
A = [9,3,9,3,9,7,9]
print(solution(A))