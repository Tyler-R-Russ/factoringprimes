import sumfullproperfactors
from sumfullproperfactors import sumfullproperfactors

#Purpose: This module calculates the sum of the factors of every number
#in a given range a to b.

def sumfullproperfactorsrange(a,b):
    lst=[]
    for i in range(a,b+1):
        #note to self: python indexing: range(a,b) gives (a,a+1,...,b-1)
        lst=lst+[sumfullproperfactors(i)]
    return(lst)
