import totient
from totient import totient
import unitsclass
from unitsclass import unitsclass
import order
from order import order

#This tells us which numbers in a group Z_n, the integers modulo n,
#are primitive roots. Primitive roots have order equal to phi, where phi is
#given by the euler totient (phi) function for the number n.

def primroots(n):
    phi = totient (n)
    lst = unitsclass (n)
    lst = filter (lambda x: order (x,n) == phi, lst)
    return (lst)








