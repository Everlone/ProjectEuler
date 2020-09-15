'''
euler_004.py
Fourth problem of the Euler Project

------------------------------------------------------------------------------
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
------------------------------------------------------------------------------

Written by Stephen Outten 07 January 2019
'''

import numpy as np


def check_palindrome(numb):
    '''
    Check whether or not the number is a palindrome. 
    If it's an odd length number, drop the middle digit.
    Then compare the two halves of the number.
    '''
    n = str(numb)
    if len(n)%2==1: 
        palindrome = n[:int(len(n)/2)] == n[int(len(n)/2)+1:][::-1]
    else:
        palindrome = n[:int(len(n)/2)] == n[int(len(n)/2):][::-1]
    
    return palindrome
    

# Cycle through all three digits number combinations
palindrome_numbs = np.array([0,0,0])
for a in range(999,100,-1):
    for b in range(a,100,-1):
        if check_palindrome(a*b): palindrome_numbs = np.vstack([palindrome_numbs,[a,b,a*b]])
a,b,c = palindrome_numbs[np.argmax(np.max(palindrome_numbs,axis=1)),:]


print('The larget palindrome is {0}, a multiple of {1} and {2}.'.format(c,a,b))

