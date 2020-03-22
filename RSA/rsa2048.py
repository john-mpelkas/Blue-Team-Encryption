import random
import math

# <---------------------------------------------------------------------
# Generating two prime number keys used for RSA encryption
# <---------------------------------------------------------------------
def genKeys():
    primeNum = genRandNum()
    while(rabinMillerTest(primeNum, 128) == False):
        primeNum = genRandNum()
    return (primeNum);

def genRandNum():
    return random.getrandbits(1024);
# <---------------------------------------------------------------------
# Rabin Miller Test
# The goal of this test is to find a non-trivial square root.
# If one is found we can assume that n will be prime.
# We will be using a witness to prove that n is a pseudo prime.
# Will return false if n is composite or true if n is a pseudo prime.
# Subjects to  better understand this test;
#   {Prime Number Theorem, Euler's Totient Function, Fermat
#   Primality test, Non-Trivial Square Roots}
# <---------------------------------------------------------------------
def rabinMillerTest(primeNum, numOfTests):
# <---------------------------------------------------------------------
# Edge Cases;
# <---------------------------------------------------------------------
    if (primeNum < 1): return False;        #Removing all negative numbers
    if (primeNum % 2 == 0): return False;   #Removing all even numbers
    if (primeNum <= 3): return True;


# <---------------------------------------------------------------------
# Factoring
# n-1 should be congurent to 2^k*q
# <---------------------------------------------------------------------

    q = primeNum - 1    #Is to be assumed not prime
    k = 0               #

    while(q % 2 == 0):  #Continue until odd number is hit
        q //= 2         #
        k += 1          #

# <---------------------------------------------------------------------
# Running multiple test with different composite witnesses.
# Return True if number is prime.
# Passing the Composite test will return FALSE
# Failing the Compoisite test will return
# <---------------------------------------------------------------------
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


# <---------------------------------------------------------------------
# RSA
# 1. Generate two prime numbers
# 2. Find the product(N) of these two numbers
# 3. ϕ(N) - Euler's phi function - Find coprime of N
#    ϕ(N) = (p-1)(q-1)
# 4. Choose e: 1<e<ϕ(N) | Coprime with N, ϕ(N)    (e,N) - Public lock
# 5. Choose d: d*e(modϕ(N)) = 1                   (d,N) - Private Key
# <---------------------------------------------------------------------

def rsa(p, q):
    n = p * q

    L = (q - 1) * (p - 1)



keyOne = 2#keyOne = genKeys()
keyTwo = 7#keyTwo = genKeys()

rsa(keyOne, keyTwo)
