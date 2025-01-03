import numberofprimefactors
from numberofprimefactors import numberofprimefactors

#Purpose: This module gives the number of prime factors for a list of numbers
#in a range from a to b.

#short for: numberofprimefactorsinarange
def numprimfactrange (a,b):
    lst=list()
    #lst=[]
    for i in range (a,b+1):
        lst.append(numberofprimefactors(i))
    return (lst)
