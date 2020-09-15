'''
euler_006.py
Sixth problem of the Euler Project

------------------------------------------------------------------------------
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
------------------------------------------------------------------------------

Written by Stephen Outten 08 January 2019
'''

a = b = 1
for i in range(2,101):
    a += i
    b += i*i
a = a*a

answer = a-b

print('The difference between the sum ofthe squares and the square of the sum for the first 100 numbers is {0}.'.format(answer))

