'''
euler_003.py
Third problem of the Euler Project

------------------------------------------------------------------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
------------------------------------------------------------------------------

Written by Stephen Outten 24 December 2017
'''

import numpy as np
import mathfuncs as mf

# numb = 13195
numb = 600851475143

answer = mf.primefactors(numb)

print('The larget prime factor of {0} is {1}'.format(numb,answer[-1]))

