import halfproperfactors
from halfproperfactors import halfproperfactors

#Purpose: This module returns true (1) if n is prime, otherwise false (0).

#Theory: A number n is prime if it has no proper factors aside from 1.
#Further, if a number n has no proper factors less than or equal to sqrt(n),
#then it is prime. We utilize that fact below.

def prime(n):
    if (n<=0): return("n must be a positive integer")
    
    lst = halfproperfactors(n)
    if len(lst)==1:
        return(1)
    else:
        return(0)

    







