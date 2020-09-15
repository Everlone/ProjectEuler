'''
euler_010.py
Tenth problem in the Project Euler series.

---------------------------------------------------------------------------
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
---------------------------------------------------------------------------

Uses the fact that any non-prime number (composite number) must have a factor which 
is smaller than it's square root.

Written by Stephen Outten 10th January 2019
'''

import numpy as np


def is_composite(numb):
    for i in range(3,np.int(np.sqrt(numb))+1,2):
        if numb%i==0: 
            return 0
    return numb


answer = 17
for i in range(9,2000000,2):
    answer += is_composite(i)  
    
print('The sum of all primes up to 2000000 is {0}.'.format(answer))

    







