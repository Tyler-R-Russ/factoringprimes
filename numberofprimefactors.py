import fullprimefactors
from fullprimefactors import fullprimefactors

#Purpose: This module gives the number of prime factors of a number n.
#Theory: This module does not use the Euler totient function.

def numberofprimefactors(n):
    lst=fullprimefactors(n)
    return (len(lst))



