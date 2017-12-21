'''
euler_001.py
First problem of the Euler Project

------------------------------------------------------------------------------
If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
------------------------------------------------------------------------------

Written by Stephen Outten 21 December 2017
'''

import numpy as np

# This is a comment
n = 1000
array3 = np.arange(0,n,3)
array5 = np.arange(0,n,5)
# answer = np.sum(np.arange(0,n,3)) + np.sum(np.arange(0,n,5)) - np.sum(np.arange(0,n,15))
answer = np.sum(np.unique(np.concatenate((array3,array5))))
print('And the answer is %i' % answer)

