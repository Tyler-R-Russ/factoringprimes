import numberofprimefactors
from numberofprimefactors import numberofprimefactors

import halfproperfactors
from halfproperfactors import halfproperfactors

#Purpose: This module returns the list of primes from 2 up to n.

#A prime has no proper factors aside from 1. Since the
#function halfproperfactors includes 1, we have to set length (len) = 1
#Further, if a number n has no proper factors less than sqrt(n),
#then it is prime. We utilize that fact below.

def primes(n):

    lst = range(2,n+1)
    i = 2
    for i in lst:
        lst=filter(lambda i:len(halfproperfactors(i))==1,lst)
    return(lst)
