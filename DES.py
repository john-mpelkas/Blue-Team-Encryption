#Initial Permutation Table
initialPermutationTable = (
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
)
#Final Permutation Table (Inverse of Initial)
finalPermutationTable = (
    40,  8, 48, 16, 56, 24, 64, 32,
    39,  7, 47, 15, 55, 23, 63, 31,
    38,  6, 46, 14, 54, 22, 62, 30,
    37,  5, 45, 13, 53, 21, 61, 29,
    36,  4, 44, 12, 52, 20, 60, 28,
    35,  3, 43, 11, 51, 19, 59, 27,
    34,  2, 42, 10, 50, 18, 58, 26,
    33,  1, 41,  9, 49, 17, 57, 25
)
#Initial permutation made on the key
keyPermutationTable1 = (
    57, 49, 41, 33, 25, 17, 9,
    1,  58, 50, 42, 34, 26, 18,
    10, 2,  59, 51, 43, 35, 27,
    19, 11, 3,  60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7,  62, 54, 46, 38, 30, 22,
    14, 6,  61, 53, 45, 37, 29,
    21, 13, 5,  28, 20, 12, 4
)
#Permutation applied on the shifted key (Second and beyond permutation (Second+))
keyPermutationTable2 = (
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
)
#Matrix Expansion (End goal is to get the 48-bit matrix
matrixExpansionTable = (
    32, 1,  2,  3,  4,  5,
    4,  5,  6,  7,  8,  9,
    8,  9,  10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
)
#S-Box Table (Substitution step)
sBoxTable = {
    0: (
        14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
        0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
        4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
        15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13
    ),
    1: (
        15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
        3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
        0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
        13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9 
    ),
    2: (
        10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
        13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
        13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
        1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12 
    ),
    3: (
        7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
        13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
        10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
        3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14
    ),
    4: (
        2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
        14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
        4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
        11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3
    ),
    5: (
        12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
        10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
        9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
        4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13
    ),
    6: (
        4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
        13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
        1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
        6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12
    ),
    7: (
        13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
        1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
        7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
        2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11
    )
}
#Straight Permutation (Made after the S-Box Substitution for each round)
straightPermutationTable = (
    16,  7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11, 4,  25
)

#Single blocks only
#Initiates the encryption by calling the functions that will generate the keys and start the rounds of encryption for the message
def encryption(message, key, decryption=False):
	assert isinstance(message, int) and isinstance(key, int)
	assert not message.bit_length() > 64
	assert not key.bit_length() > 64
	
	key = permutation(key, 64, keyPermutationTable1) #This call will permute the 64-bit key to 56-bits
	
	#Splitting the key in half to generate the 16 keys
	key1 = key >> 28
	key2 = key & (2**28-1)
	sixteenKeys = keyGeneration(key1, key2) #56-bit key --> 48-bits
	
	block = permutation(message, 64, initialPermutationTable)
	left = block >> 32
	right = block & (2**32-1)
	
	#Feistel cipher (16 rounds)
	leftPrevious = left
	rightPrevious = right
	for x in range (1,17):
		if decryption: #Decryption does the cipher in reverse
			x = 17-x
		leftRound = rightPrevious
		rightRound = leftPrevious ^ roundFunction(rightPrevious, sixteenKeys[x])
		leftPrevious = leftRound
		rightPrevious = rightRound
	
	#combining the left and right sides	
	cipherBlock = (rightRound<<32) + leftRound
	
	#final permutation
	cipherBlock = permutation(cipherBlock, 64, finalPermutationTable)
	
	return cipherBlock
	
#Feistel cipher - 16 rounds of encryption
def roundFunction(b, k): #Accepts block and key as parameters
	#Expands the block from 32 to 48 bits using the table for Matrix Exansion (matrixExpansionTable)
	b = permutation(b, 32, matrixExpansionTable)
	
	#xor
	b ^= k
	
	#Creates the 8 groups of 6-bits
	bBlocks = [((b & (0b111111 << valueToShiftBy)) >> valueToShiftBy) for valueToShiftBy in (42,36,30,24,18,12,6,0)]
	
	#Start of S-Boxes
	for x, block in enumerate(bBlocks):
		row = ((0b100000 & block) >> 4) + (0b1 & block)
		column = (0b11110 & block) >> 1
		bBlocks[x] = sBoxTable[x][16*row+column]
		
	#string the blocks together
	bBlocks = zip(bBlocks, (28,24,20,16,12,8,4,0))
	b = 0
	for block, shiftLeftByValue in bBlocks:
		b += (block << shiftLeftByValue)
	
	#Straight permutation
	b = permutation(b, 32, straightPermutationTable)
	
	return b

#Creates a string 
def permutation(block, blockLength, table):
	blockString = bin(block)[2:].zfill(blockLength)
	permutationArray = []
	for x in range(len(table)):
		permutationArray.append(blockString[table[x]-1])
	return int(''.join(permutationArray), 2)
	
#Creates the 16 keys
def keyGeneration(key1, key2):
	sixteenKeys = dict.fromkeys(range(0,17))
	leftRotationValues = (1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1)
	
	#left rotation, shift the value by certain number of bits between aBits and bBits
	rotation = lambda value, aBits, bBits: \
	(value << aBits%bBits) & (2**bBits-1) | \
	((value & (2**bBits-1)) >> (bBits-(aBits%bBits)))
	
	#rotation
	key1 = rotation(key1, 0, 28)
	key2 = rotation(key2, 0, 28)
	
	sixteenKeys[0] = (key1, key2)
	
	for x, valueToRotateBy in enumerate(leftRotationValues):
		x+=1
		k1 = rotation(sixteenKeys[x-1][0], valueToRotateBy, 28)
		k2 = rotation(sixteenKeys[x-1][1], valueToRotateBy, 28)
		sixteenKeys[x] = (k1, k2)
	#remove key[0]
	del sixteenKeys[0]
	
	#Apply keyPermutationTable2 to permute the 56-bit key to 48-bit
	for x, (key1, key2) in sixteenKeys.items():
		sixteenKeysX = (key1 << 28) + key2
		sixteenKeys[x] = permutation(sixteenKeysX, 56, keyPermutationTable2)
	
	return sixteenKeys

#64-bit only for both key and message	
exampleKey = 0x0fce2fa545f36ec30 
exampleKey2 = 0x1d7d5920ac6f3ae
exampleMessage = 0x8e40dcac600c04b7
exampleMessage2 = 0x064006400640064

def run(key, message):
    print('Key: {:x}'.format(key))
    print('Message: {:x}'.format(message))
    print(' ')
    textInCipher = encryption(message, key)
    print('Encrypted: {:x}'.format(textInCipher))
    textInPlain = encryption(textInCipher, key, decryption=True)
    print('Decrypted: {:x}'.format(textInPlain))
	
run(exampleKey, exampleMessage)
print('---------------------------------')
run(exampleKey2, exampleMessage2)