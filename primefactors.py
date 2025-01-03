import totient
from totient import totient

import fullproperfactors
from fullproperfactors import fullproperfactors

#Purpose: This gives a list of the prime factors of a number.
#If the number is prime, it returns the number itself.
#Theory: This code is likely inefficient.

def primefactors(n):
    if (n<=0): return("n must be a positive integer")

    lst = fullproperfactors(n)
    del lst[0]  #Namely, we want to exclude the proper factor "1" since it is not prime
    i=1
    for i in lst:
        lst = list(filter (lambda i:totient(i)==i-1,lst))
        
    if len(lst)==0:
        lst=[n]

    return(lst)
