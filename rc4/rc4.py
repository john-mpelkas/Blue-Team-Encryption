#KSA is key-scheduling algorithm
#PRGA is pseudo-random generation algorithm
#key is one byte
#s is 256-bytes
#t is temporary 256-byte vector




#sets s equal to values 0 to 255
def ksa (key):
    s = list(range(0,255))
    j = 0
    for i in range(0 ,255):
        j = (j + s[i] + key[i% len(key)])% 256
        #swaps s at i and s at j
        s[i], s[j] = s[j], s[i]

    return s

def prga (s):
    i = 0
    j = 0
    while True:
        i = (i + 1)%256
        j = (j + s[i])%256

        # swaps s at i and s at j
        s[i], s[j] = s[j], s[i]
        #holds value of s at i plus s at j
        t = (s[i] + s[j])%256
        k = s[t]

        yield k

#generates the keystream
def get_ks(key):
    s = ksa(key)
    return prga(s)


def encrypt(key, plaintext):


def decrypt(key, ciphertext):


def main():

