#useful code:
#sys.path.append('factoringprimes')
#import fullproperfactors
#from fullproperfactors import fullproperfactors




#In an earlier version, the following code was needed:
# lst = sorted(list(set(lst)))


#Alternative version:
##def fullproperfactors(n):
##     i = 2
##     lst = halfproperfactors(n)
##     lst.reverse()
##     c = len(lst)
##     
##     for i in range (0,c):
##                    lst[i] = n/lst[i]
##                    
##     string = halfproperfactors(n)
##     string2 = string + lst
##     finalstring = sorted(list(set(string2)))
##     return(finalstring)
