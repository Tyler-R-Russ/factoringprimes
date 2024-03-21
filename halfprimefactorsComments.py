#useful code
#sys.path.append('numbertheory/factoringprimes')
#import halfprimefactors
#from halfprimefactors import halfprimefactors

#for xrange see:
#http://pythoncentral.io/how-to-use-pythons-xrange-and-range/
#http://pythoncentral.io/python-generators-and-yield-keyword/


#alternate code ideas:
##def halfprimefactors(n):
##     i = 2
##     lst = xrange (2,int(floor(sqrt(n)+1)))
##     lst = [x for x in lst if gcd (x,n) == x]
##     return(lst)
##




#modification ideas for efficiency:
  #this list comprehension: lst = [x for x in lst if gcd (x,n) == x]
    #is slower (I think) (verify)
    


#Consider rewriting with a for and filter command instead. Which is faster?
##def halfprimefactors(n):
##     i = 2
##     lst = xrange (2,int(floor(sqrt(n)+1)))
##     for i in lst:
##          lst = filter(lambda i:gcd (i,n) == i,lst)
##     return(lst)
