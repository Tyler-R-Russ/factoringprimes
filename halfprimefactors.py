import primesrange
from primesrange import primesrange

from math import gcd
from math import sqrt
from math import ceil
from math import floor #returns float


#Purpose: This module returns the prime factors of a natural number n
#less than or equal to sqrt(n).

#Theory: Half of the proper factors of a number n are less than or equal to
#the square root of that number sqrt(n).


def halfprimefactors(n):
     if (n<=0): return("n must be a positive integer")
     
     x = 2
     lst = primesrange(2,int(floor(sqrt(n)+1))) #The built-in 'floor' function
     #returns a float object; we force its class to integer (int).
     lst = [x for x in lst if n%x == 0]
     return(lst)
