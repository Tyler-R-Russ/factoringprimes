from math import gcd
from math import sqrt
from math import ceil
from math import floor

import halfproperfactors
from halfproperfactors import halfproperfactors


#Purpose: This module creates a complete list of the
#factors of a number n, including the number 'n' as well.

#Theory: Half of the proper factors are less than sqrt(n)
#The remaining proper factors can be found by division;
#namely if divisor d|n is in {1,...,floor[sqrt(n)]}
#then the complementary divisor d' >= floor[sqrt(n)] is found by the division
#d' = n/d.


def fullfactors(n):
     if (n<=0): return("n must be a positive integer")
     
     lst = halfproperfactors(n) #module 'halfproperfactors'
     #gives us the proper factors from 1 to sqrt(n).
     string = halfproperfactors(n) #factors always come in pairs
     c = len(lst)

     #This creates the upper half list of factors:
     for i in reversed(range (0,c)): #reverse the list from halfproperfactors
          m=int(n/string[i]) #append n/string[i] calculated from string[i] 
          lst.append(m)
     lst = sorted(list(set(lst))) #apply lst = sorted(list(set(lst)))
     #convert to a set to eliminate redundancies (if n is a perfect square),
     #change the type to list and sort it.
     return(lst)
