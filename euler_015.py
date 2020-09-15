'''
euler_015.py
Fifthteenth problem in the Project Euler series.

---------------------------------------------------------------------------
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
---------------------------------------------------------------------------

Written by Stephen Outten 21 January 2019
'''

from scipy.special import perm
import time

start = time.time()


ngrid = 20
answer = int(perm(2*ngrid,2*ngrid)/(perm(ngrid,ngrid)**2))

print('The number of possible routes for a {0}x{0} grid is {1}.'.format(ngrid,answer))

print('This took {0:.2f} seconds.'.format(time.time()-start))







