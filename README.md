# factoringprimes

This is short-hand for the more descriptive title, "Factoring numbers and identifying primes and prime factors".

These modules have been written in Python, originally in Python 2.7.5.1 and then edited for Python 3. This code should compile and run with Python version 3.6. Please message me if you have difficulty running the code (truss3@gmu.edu) following the steps below.

## Motivation and Use: 

I began writing these files to have desktop access to factoring software.
Also, my research involved identifying primes, ranges of primes, sums of factors of numbers, etc., so programs for specific purposes were needed.

The modules in this folder (factoringprimes) have the function of finding a number's proper and prime factors, finding primes in a given range and related computations.

## Description: 

This folder (project) contains a number of Python modules which are interdependent. The hierarchy of these modules is laid out in a separate file (pdf) "Dependency_Diagram_factoringprimes.pdf"

(See the section below, "Calling each Module" for the specifics of running each module.)

## How to Run the Project:

These modules have not been formatted into a Python package.

To run the programs, do the following:

1. Download the folder. 

If the folder is not automatically incorporated into your Python path, then

2. Add the folder to the path using the following code (for an individual session):

import sys
sys.path.append('factoringprimes')

If this call to sys.path.append does not work, you may need to use a call to specify the location of the directory, similar in spirit to the following:
sys.path.append('path/to/factoringprimes')

Once the folder (directory) is in your Python path, you can 

3. Import each module in the customary way in your Python executable screen:

import module

from module import module

### Example importing a module

In this folder, each module name matches the folder name. Here is an example:

To import the module fullprimefactors, use the following code:

import fullprimefactors

from fullprimefactors import fullprimefactors

You should be able to run any module following the steps given above.

## Calling each Module:

The information below describes how to call each module and the specific calculation each module performs.

You can find this information in each separate python module (e.g. by selecting 'edit' with Idle).
For convenience it is included below.
The modules are described in alphabetical order.

<details>
  <summary>factors:</summary>
  
factors($n$)
  
$n$ is an integer

Purpose: This code generates the factors of a (natural) number $n$.
</details>
<details>
  <summary>
    fullprimefactors:
  </summary>
  
fullprimefactors($n$)
  
$n$ is an integer

Purpose: This module returns the prime factors of a natural number $n$.
</details>
<details>
  <summary>
    fullfactors:
  </summary>
  
fullfactors(n) 
  
$n$ is an integer

Purpose: This module creates a complete list of the factors of a number, including the number '$n$' as well.
</details>
<details>
  <summary>
    halfprimefactors:
  </summary>
  
halfprimefactors($n$)
  
$n$ is an integer

Purpose: This module returns the prime factors of a natural number n less than or equal to $\sqrt{n}$.
</details>
<details>
  <summary>
    halfproperfactors:
  </summary>
  
halfproperfactors(n)
  
$n$ is an integer

Purpose: This module calculates half of the proper factors of a natural number $n$ from $1$ (one) up to $\sqrt{n}$.
</details>
<details>
  <summary>
    mersennerange:
  </summary>
  
mersennerange($a,b$)
  
$a < b$ are integers

This module provides the Mersenne primes within a bound between the two number $2^{a} - 1$ and $2^{b} - 1$ (inclusive).
</details>
<details>
  <summary>
    numberofprimefactors:
  </summary>
  
numberofprimefactors(n)
  
$n$ is an integer

Purpose: This module gives the number of prime factors of a number n.
</details>
<details>
  <summary>
    numprimfactrange:
  </summary>
  
numprimfactrange ($a,b$)
  
$a < b$ are integers

Purpose: This module gives the number of prime factors for a list of numbers in a range from $a$ to $b$.
</details>
<details>
  <summary>
    prime:
  </summary>
  
prime($n$)
  
$n$ is an integer

Purpose: This module returns true ($1$) if $n$ is prime, otherwise false ($0$).
</details>
<details>
  <summary>
    primefactors:
  </summary>
  
primefactors($n$)
  
$n$ is an integer

Purpose: This gives a list of the prime factors of a number. If the number is prime, it returns the number itself.
</details>
<details>
  <summary>
    primes:
  </summary>
  
primes($n$)
  
$n$ is an integer
  
Purpose: This module returns the list of primes from $2$ up to $n$.
</details>

<details>
  <summary>
    primesrange:
  </summary>
  
primesrange($a,b$)
  
$a < b$ are integers
     
Purpose: This module lists the positive primes in a range from $a$ to $b$.
</details>

<details>
 <summary>
    properfactors:
  </summary>
  
properfactors($n$)
  
$n$ is an integer
     
Purpose: This module generates the proper factors of a number $n$ (which excludes $n$ itself).
</details>

<details>
  <summary>
    sumfullfactors:
  </summary>
  
sumfullfactors(n)
  
$n$ is an integer

Purpose: This program finds the sum of the factors of a number $n$, including $n$.
</details>

<details>
  <summary>
    sumfullfactorsrange:
  </summary>
  
sumfullfactorsrange($a,b$)
  
$a < b$ are integers

Purpose: This module calculates the sum of the factors of every number in a given range $a$ to $b$.
</details>

<details>
 <summary>
    totient:
  </summary>
  
totient($n$)
  
$n$ is an integer

Purpose: This module calculates Euler's totient function for the number $n$.
</details>
