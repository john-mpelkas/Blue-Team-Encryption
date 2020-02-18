def asciiWrapper(char, key):
    asciiVal = ord(char)
    asciiVal += key

    if(ord(char) < 97 or ord(char) > 122):
        return char
    if (asciiVal > 122):
        asciiVal = (asciiVal%122)+96
    return chr(asciiVal)

def arrJoiner(textCharArr):
    text = ""
    for element in textCharArr:
        text += element
    return text

def caesarCipher(text, key):
    textCharArr = (list(text))
    for element in range(0, len(text)):
        textCharArr[element] = asciiWrapper(textCharArr[element], key)
    return arrJoiner(textCharArr)


#example

key = 2
f = open("PlainText.txt", "r")

if(f.mode == 'r'):
    contents = f.read()
f.close()

f = open("CipherText.txt", "w+")
f.write(caesarCipher(contents.lower(), key))
f.close()
