#RSA Encryption (Rivest-Shamir-Adleman)

**Main.py**

This file is the driver class of the application. This class will generate two RSA keys that will be used during this encryption. The size of the key can be increased or decreased by changing the values being passed to *RsaAlgo.py*. The table below shows the run time in seconds based on the size of the key being generated in bits.

|  Number size (Bits)   |  RunTime (Seconds) |
|-----------------------|--------------------|
|         512           |    1.219           |
|        1024           |    5.790           |
|        2048           |   60.714           |

This application requires that you enter a message, *in the form of a number*, to encrypt. The message is then encoded to be printed out to the console. Followed by the decoding of the message which is also printed to the console. These messages are using the RSA encryption method in order to encrypt and decrypt these messages.

**dkeybank.txt & ekeybank.txt**

These files are used to stored the encryption and decryption key pairs to be used in the encryption and decryption process.

**PrimeNumberGenerator.py**

This function is used twice to generate the two prime numbers to be used in calculating all the needed values in the **RsaAlgo.py**. This program finds these massive numbers using the Rabin Miller Primality test. This primality test adds onto the Fermat primality test which increased the success rate of finding a true prime number.

**RsaAlgo.py**

This file was created to be a controller class for the RSA algorithm. In this algorithm using the two prime numbers generate two unique numbers that will become the part of the pair keys used to encrypt and decrypt messages.
