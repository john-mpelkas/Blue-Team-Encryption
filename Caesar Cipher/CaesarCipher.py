

# Function to handle ascii operations. This program will only encrypt characters
# from the English alphet excluding special characters. Once the ascii value
# exceeds 122 it will wrap back around to the begining of the ascii table
def asciiWrapper(char, key):

    asciiVal = ord(char)
    asciiVal += key

    if(ord(char) < 97 or ord(char) > 122):
        return char
    if (asciiVal > 122):
        asciiVal = (asciiVal%122)+96

    return chr(asciiVal)

def arrJoiner(textCharArr):
    text =""
    for element in textCharArr:
        text += element
    return text

def caesarCipher(text, key):

    textCharArr = (list(text))
    for element in range(0, len(text)):
        textCharArr[element] = asciiWrapper(textCharArr[element], key)

    return arrJoiner(textCharArr)

def main():
    #test = "Ice cream (derived from earlier iced cream or cream ice) is a sweetened frozen food typically eaten as a snack or dessert. It may be made from dairy milk or cream and is flavored with a sweetener, either sugar or an alternative, and any spice, such as cocoa or vanilla. Colourings are usually added, in addition to stabilizers."
    #test = "aAbbcc the dog"
    key = 2

    f = open("PlainText.txt", "r")
    if(f.mode == 'r'):
        contents =f.read()
    f.close()

    f = open("CipherText.txt", "w+")
    f.write(caesarCipher(contents.lower(), key))
    f.close()



if __name__ == "__main__":
    main()
