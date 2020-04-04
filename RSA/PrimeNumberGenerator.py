import random
import math
# <---------------------------------------------------------------------
# Generating two prime number keys used for RSA encryption
# <---------------------------------------------------------------------
def genKeys(n):
    primeNum = random.getrandbits(n);
    while(rabinMillerTest(primeNum, 128) == False):
        primeNum = random.getrandbits(n);
    return (primeNum);

# <---------------------------------------------------------------------
# Rabin Miller Test
# This test will find a prime number by testing the previous number
#
# Subjects to  better understand this test;
#   {Prime Number Theorem, Euler's Totient Function, Fermat
#   Primality test, Non-Trivial Square Roots}
# <---------------------------------------------------------------------
def rabinMillerTest(primeNum, numOfTests):

# Edge Cases;
    if (primeNum < 1): return False;        #Removing all negative numbers
    if (primeNum % 2 == 0): return False;   #Removing all even numbers
    if (primeNum <= 3): return True;        #2&3 will return as prime

    q = primeNum - 1    #Is to be assumed not prime
    k = 0               #Will be used to determine k below
# q ≅ to 2^k*q
    while(q % 2 == 0):  # while power can be taken out
        q //= 2
        k += 1

#rabinMillerTest
    for i in range(numOfTests):
# Composite test: START
        a = random.randint(2, primeNum - 1)     #Composite witness
        x = pow(a, q, primeNum)                 #Test 1

        if (x != 1 and x != primeNum - 1):
            j = 1

            while (j < k and x != primeNum - 1):
                x = pow(x, 2, primeNum)         #Test 2
                if(x == 1):
                    return False;
                j += 1

            if (x != primeNum - 1):
                return False;
# Composite test: END
    return True;
