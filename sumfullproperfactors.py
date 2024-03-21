import fullproperfactors
from fullproperfactors import fullproperfactors

#Purpose: This program finds the sum of the factors of a number n, including n.
#Theory: The method is brute force and does not utilize the prime factorization of n.

def sumfullproperfactors(n):
    lst = fullproperfactors(n)
    return(sum(lst))






