from math import floor #returns float


#Purpose: This module returns the prime factors of a natural number n.
#Theory: Half of proper factors of number n are less than or equal to sqrt(n).
#At most one (linear) prime factor is larger than sqrt(n).


def fullprimefactors(n):
     if (n<=0): return("n must be a positive integer")
     
     i = 2
     maxx = int(floor(sqrt(n)))
     m = n
     j = 2
     lst=[]
     for j in range (i,maxx+1): #list indexing in python, upper bound
         if bool(prime(j)==1)*bool(m%j==0)==1: #"And" operator is product
             lst.append(j)
             while bool(m%j==0)==1: #while loop reduces full multiplicity
                 m = m/j  
         else:
             maxx = int(floor(sqrt(m))) #Built-in 'floor' function returns a
             #float object; we force its class to integer (int). We update
             #the maxx to the reduced number m
             i = i+1
             j=j+1
     if m != 1: #at most one (linear) prime factor m greater than sqrt(n)
         lst.append(m)
     return(lst)
