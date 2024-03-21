#useful code:
#sys.path.append('factoringprimes')
#import halfproperfactors
#from halfproperfactors import halfproperfactors

#for xrange see:
#http://pythoncentral.io/how-to-use-pythons-xrange-and-range/
#http://pythoncentral.io/python-generators-and-yield-keyword/




#rewritten with a list comprehension
##def halfproperfactors(n):
##     i = 2
##     lst = xrange (2,int(floor(sqrt(n)+1)))
##     for i in lst:
##          lst = filter(lambda i:gcd (i,n) == i,lst)
##     return(lst)



#this works::
##def halfproperfactors(n):
##     i = 2
##     for i in range (2,int(floor(sqrt(n)+1))):
##                    lst = range (2,int(floor(sqrt(n)+1)))
##                    lst = filter(lambda i:gcd (i,n) == i,lst)
##     return(lst)
