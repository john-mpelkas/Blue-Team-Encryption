import random
import math
import base64
import PrimeNumberGenerator

# <---------------------------------------------------------------------
# A. RSA
# 1. Find the product(N) of these two numbers
# 2. ϕ(N) - Euler's phi function - Find coprime of N
#    ϕ(N) = (p-1)(q-1)
# 3. Choose e: 1<e<ϕ(N) | e Coprime of N and ϕ(N)    (e,N) - Public lock
# 4. Choose d: d*e(modϕ(N)) = 1                      (d,N) - Private Key
# <---------------------------------------------------------------------

def rsa(p, q): #p&q generated prime numbers
    print ("Calculating n . . .")
    n = p * q
    print ("Calculating eulerPhi . . .")
    eulerPhi = (q - 1) * (p - 1)
    print ("Calculating e . . .")
    e = publicLock(n, eulerPhi)
    print ("Calculating d . . .")
    d = privateKey(e, eulerPhi, n)
    while (e == d):
        print ("Calculating e . . .")
        e = publicLock(n, eulerPhi)
        print ("Calculating d . . .")
        d = privateKey(e, eulerPhi, n)

    f = open("ekeybank.txt", "w")
    f.write(str(e))
    f.write("\n")
    f.write(str(n))
    f.close()

    f = open("dkeybank.txt", "w")
    f.write(str(d))
    f.write("\n")
    f.write(str(n))
    f.close()

# <---------------------------------------------------------------------
# B. PublicLock 'e'
# <---------------------------------------------------------------------

def publicLock(n, eulerPhi):

    e = random.randint(2,eulerPhi - 1)
    while (findCoPrime(e, n, eulerPhi) == False):
        e = random.randint(2,eulerPhi - 1)

    return e


def findCoPrime(x, y, z):
    hcf1 = hcf(x, y)
    hcf2 = hcf(x, z)
    if (hcf1 == 1 and hcf2 == 1):
        return True
    return False

def hcf(x, y):
    while(y != 0):
        x, y = y, x % y

    return x

# <---------------------------------------------------------------------
# C. Private Key 'd'
# <---------------------------------------------------------------------
def privateKey(e, eulerPhi, n):
    d = modInverse(e,eulerPhi)
    return d


def modInverse(a, m) :
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if hcf(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
