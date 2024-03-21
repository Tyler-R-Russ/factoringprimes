#useful code:
#sys.path.append('factoringprimes')
#import mersennerange
#from mersennerange import mersennerange


#http://stackoverflow.com/questions/11283220/memory-error-in-python
#online source for suggested algorithm improvement
#http://pythoncentral.io/python-generators-and-yield-keyword/



#We have rewritten primesrange and halproperfactors to have xrange
#instead of range in their codes.

#The following gave MemoryError for mersennerange(59,59) on intel core i5 Dell
#Rewrote primesrange and halproperfactors, now mersennerange(59,59) exits
#after about 40 minutes
#mersennerange(61,61) exited after about 2 hours with number
#Portable Python >>> mersennerange(61,61)
#[2305843009213693951L]


#Code run-time data:
#The following code gives MemoryError for mersennerange(51,53) on my intel
#Core i5 DELL computer (February 11, 2017)


##def mersennerange(a,b):
##    lst = primesrange(a,b+1)
##    lst = [2**x-1 for x in lst if len(halfproperfactors(2**x-1))==0]
##    return(lst)


#The following post
##http://stackoverflow.com/questions/11283220/memory-error-in-python
#gives the following code improvement, which we may want to imitate
#and incorporate to our code.


##s = raw_input()
##a=len(s)
##for i in xrange(0, a):
##    for j in xrange(0, a):
##        if j >= i:
##            if len(s[i:j+1]) > 0:
##                sub_strings.append(s[i:j+1])
##seems to be very inefficient and expensive for large strings.
##
##Better do
##
##for i in xrange(0, a):
##    for j in xrange(i, a): # ensures that j >= i, no test required
##        part = buffer(s, i, j+1-i) # don't duplicate data
##        if len(part) > 0:
##            sub_Strings.append(part)

#This code was executed on 2/11/2017 (not on the default date below)
##mersennerange(59,59)
##Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win
##32
##Type "help", "copyright", "credits" or "license" for more information.
##Portable Python >>> sys.path.append('numbertheory')
##Portable Python >>> import mersennerange
##Portable Python >>> from mersennerange import mersennerange
##Portable Python >>> mersennerange(1,10)
##[1, 3, 7, 31, 127]
##Portable Python >>> mersennerange(59,59)
##[]
##Portable Python >>> mersennerange(61,61)
##[2305843009213693951L]
##Portable Python >>>

##Data on 1/18/20
##
##Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win
##32
##Type "help", "copyright", "credits" or "license" for more information.
##Portable Python >>> sys.path.append('numbertheory/factoringprimesperfect')
##Portable Python >>> import mersennerange
##Portable Python >>> from mersennerange import mersennerange
##Portable Python >>> mersennerange(1,10)
##[3, 7, 31, 127]
##Portable Python >>> mersennerange(10,20)
##[8191, 131071, 524287]
##Portable Python >>> mersennerange(20,30)
##[2147483647L]
##Portable Python >>> mersennerange(30,40)
##[2147483647L]
##Portable Python >>> mersennerange(31,40)
##[2147483647L]
##Portable Python >>>
##
##Need to interpret the results above that are identical. We have lost information.

