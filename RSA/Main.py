import rsa512
import PrimeNumberGenerator

# Generating new keys
# Keys will be stored in;
#   dkeybank.txt & ekeybank.txt
rsa512.rsa(PrimeNumberGenerator.genKeys(512), PrimeNumberGenerator.genKeys(512))

# Messages are generally numbers when using RSA encryption
msg = int(input("Enter a message(number): "))

# Getting keys from ekeybank to encrypt file
f = open('ekeybank.txt', 'r')
e = int(f.readline())
n = int(f.readline())
f.close()

emsg = pow(msg, e, n)
print ("Encrypted message: ",emsg)

# Retriving decryption key from dkeybank.txt
f = open('dkeybank.txt', 'r')
e1 = int(f.readline())
f.close()

dmsg = pow(emsg, e1, n)
print ("Decrypted Message: ", dmsg)
