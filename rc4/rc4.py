# KSA is key-scheduling algorithm
# PRGA is pseudo-random generation algorithm
# key is one byte
# s is 256-bytes
# t is temporary 256-byte vector



import codecs


# sets s equal to values 0 to 255 in a list
def ksa(key):
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)])% 256
        # swaps s at i and s at j
        s[i], s[j] = s[j], s[i]

    return s


def prga(s):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256

        # swaps s at i and s at j
        s[i], s[j] = s[j], s[i]
        # holds value of s at i plus s at j
        t = (s[i] + s[j]) % 256
        k = s[t]
        # yield returns multiple times
        yield k


# generates the keystream
def get_ks(key):
    s = ksa(key)
    return prga(s)


# text is array of unicode values
# key is taken as a plaintext string
# key is then changed to a list of unicode values
def encrypt_logic(key, text):
    key = [ord(c) for c in key]
    keystream = get_ks(key)

    res =[]

    # 02X converts unicode vals into hex
    for c in text:
        value = ("%02X" % (c ^ next(keystream)))
        res.append(value)
    # returns a new string of the hex values
    return ''.join(res)


def encrypt(key, plaintext):
    plaintext = [ord(c) for c in plaintext]
    return encrypt_logic(key, plaintext)


def decrypt(key, ciphertext):
    ciphertext = codecs.decode(ciphertext, 'hex_codec')
    res = encrypt_logic(key, ciphertext)
    return codecs.decode(res,'hex_codec').decode('utf-8')


def main():
    key = 'key'
    plaintext = 'Encrypt this'

    ciphertext = encrypt(key, plaintext)
    print(f'Plaintext: {plaintext}')
    print(f'Ciphertext: {ciphertext}')

    decrypted = decrypt(key, ciphertext)
    print(f'Decrypted: {decrypted}')

    if plaintext == decrypted:
        print('This algorithm works')
    else:
        print('Nope')


if __name__ == '__main__':
    main()
