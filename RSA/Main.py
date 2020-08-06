import RsaAlgo
import PrimeNumberGenerator
import datetime

# Generating new keys
# Keys will be stored in;
#   dkeybank.txt & ekeybank.txt

begin_time = datetime.datetime.now()
RsaAlgo.rsa(PrimeNumberGenerator.genKeys(2048), PrimeNumberGenerator.genKeys(2048))


print(datetime.datetime.now() - begin_time)

# Going to encrypt some number
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
