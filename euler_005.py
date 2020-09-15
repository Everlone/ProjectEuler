'''
euler_005.py
Fifth problem of the Euler Project

------------------------------------------------------------------------------
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
------------------------------------------------------------------------------

Written by Stephen Outten 08 January 2019
'''

import numpy as np
import mathfuncs as mf

numbs = []
for i in range(2,21):
    facts = mf.primefactors(i)
    for j in numbs: 
        if j in facts:
            facts = np.delete(facts, np.where(facts==j)[0][0])
    numbs.extend(facts)

answer = np.prod(numbs)

print('The smallest number divisible by all numbers from 1 to 20 is {0}.'.format(answer))

