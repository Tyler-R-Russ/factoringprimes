import sumfullfactors
from sumfullfactors import sumfullfactors

#Purpose: This module calculates the sum of the factors of every number
#in a given range a to b.

def sumfullfactorsrange(a,b):
    lst=[]
    for i in range(a,b+1):
        #note to self: python indexing: range(a,b) gives (a,a+1,...,b-1)
        lst=lst+[sumfullfactors(i)]
    return(lst)
