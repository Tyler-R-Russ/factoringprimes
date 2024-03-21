from fractions import gcd
from math import sqrt
from math import ceil
from math import floor


#Purpose: This module calculates half of the proper factors of a natural number n
#from 1 (one) up to sqrt(n).

#Theory: This module is more efficient than the module 'factors'.
#The number of calls to the function gcd grows at a sublinear rate
#of order O(sqrt(n)).


def halfproperfactors(n):
     lst = xrange (2,int(floor(sqrt(n)+1))) #python command 'floor' returns
     #a float object; we force its class to integer (int).
     lst = [x for x in lst if gcd (x,n) == x]
     lst.insert(0,1) #Here, we include 1 as a proper factor
     return(lst)





