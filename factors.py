from math import gcd

#Purpose: This code generates the factors of a (natural) number n.

#Note: It uses the built-in gcd function.
#Theory: The approach is direct, and likely inefficient, using a filter on a list.
#It evaluates the gcd in O(n) calls to gcd.

def factors(n):
     if (n<=0): return("n must be a positive integer")
     
     i = 1
     for i in range (1, n):
                    lst = range (1,n+1)
                    lst = list(filter(lambda i:gcd (i,n) == i,lst))
     return (lst)
