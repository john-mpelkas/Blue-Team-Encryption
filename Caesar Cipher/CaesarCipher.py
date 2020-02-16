


# def asciiWrapper(char):
#     tempVal = ord(char)
#     tempVal += 1
#     #print (tempVal)
#     return chr(tempVal)

def caesarCipher(text, key):

    print (list(text[2]))
    list(text[2]) = 'z'

def main():
    test = "aabbcc dog"
    key = 1
    caesarCipher(test, key)



if __name__ == "__main__":
    main()
