import fullfactors
from fullfactors import fullfactors

#Purpose: This program finds the sum of the factors of a number n, including n.
#Theory: The method is brute force and does not utilize the prime factorization of n.

def sumfullfactors(n):
    lst = fullfactors(n)
    return(sum(lst))
