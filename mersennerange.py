import halfproperfactors
from halfproperfactors import halfproperfactors

import primesrange
from primesrange import primesrange

#This module provides the Mersenne primes within a bound between
#two number 2^a - 1 and 2^b - 1 where a,b are given as input.

def mersennerange(a,b):
    lst = primesrange(a,b+1)
    lst = [2**x-1 for x in lst if len(halfproperfactors(2**x-1))==1]
    #i.e., 1 (one) is the only proper factor
    return(lst)
