'''
euler_007.py
Seventh problem of the Euler Project

------------------------------------------------------------------------------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
------------------------------------------------------------------------------

Written by Stephen Outten 08 January 2019
'''

import numpy as np
import mathfuncs as mf
import time

start = time.time()

def is_prime(numb):
    if numb in [2,3,5,7]: 
        return True
    elif numb<9:
        return False
    for i in range(3,int(np.sqrt(numb))+1,2):
        if numb/i==numb//i:
            return False
    return True


primes = [2]
val = 3
while len(primes)<10001:
    if is_prime(val): primes.append(val)
    val += 2    

answer = primes[10000]

print('The 10,0001st prime number is {0}.'.format(answer))

print('This took {0} seconds.'.format(time.time()-start))

