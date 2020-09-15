'''
euler_014.py
Fourteenth problem in the Project Euler series.

---------------------------------------------------------------------------
The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
---------------------------------------------------------------------------

Written by Stephen Outten 21 January 2019
'''

import numpy as np
import mathfuncs as mf
import time

start = time.time()

lengths = [[numb,len(mf.collatz(numb))] for numb in range(2,1000000)]
lengths = np.array(lengths)
answer = lengths[np.where(lengths[:,1] == np.max(lengths[:,1]))]

print('The number below 1,000,000 that gives the longest Collatz chain is {0}.'.format(answer))

print('This took {0:.2f} seconds.'.format(time.time()-start))







