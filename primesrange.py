import halfproperfactors
from halfproperfactors import halfproperfactors

#Purpose: This module lists the positive primes in a range from a to b.

def primesrange(a,b):
    if a <= 1:
        a=2
    else: a=a
    lst = xrange(a,b+1) #Python indexing, modify the range to (a,b+1).
    lst = [x for x in lst if len(halfproperfactors(x))==1]
    #i.e.; if 1 is the only proper factor
    return(lst)


