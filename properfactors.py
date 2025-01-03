from math import gcd
from math import sqrt
from math import ceil
from math import floor

#Purpose: This module generates the proper factors of a number n (which excludes n)

#Theory: A number i < n is a proper factor of a number n if their gcd, gcd(i,n) is i.
#The number 'n' itself is not included as it is not a proper factor.
#This code is direct (brute force) and inefficient.
#The code for modules 'halfproperfactors' and 'fullproperfactors'
#is more efficient.


def properfactors(n):
     i = 2
     for i in range (2, n-1):
                    lst = range (2,n)
                    lst = list(filter(lambda i:gcd (i,n) == i,lst))
                    lst.insert(0,1) #Here, we include 1 as a proper factor
     return (lst)
