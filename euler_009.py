'''
euler_009.py
Ninth problem in the Project Euler series.

---------------------------------------------------------------------------
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
---------------------------------------------------------------------------

Written by Stephen Outten 09 January 2019
'''

import numpy as np
from itertools import combinations

sqrs = np.arange(1,1000)**2
sqr_trip = [[i[0],i[1],np.sum(i)] for i in combinations(sqrs, 2) if sum(i) in sqrs]
triplets = np.sqrt(sqr_trip)
triplet1k = triplets[np.sum(triplets,1)==1000][0]
answer = np.prod(triplet1k)

print("The Pythagorean triplet which sum to 1000 is {0}, {1}, and {2}, and it's product is {3}.".format(np.int(triplet1k[0]),np.int(triplet1k[1]),np.int(triplet1k[2]),np.int(answer)))


    







