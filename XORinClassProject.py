characters = [
    # lowercase characters
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # uppercase characters
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # space and symbols
    ' ',',','.','?','!','@','#','$','&','*','(',')'
]

# use this method to encode an alphabet character into a binary string
def encode(character):
    charIndex = characters.index(character)
    return '{0:06b}'.format(charIndex)

# use this method to decode a binary string into an alphabet character
def decode(binary):
    charIndex = int(binary, 2)
    return characters[charIndex]

def XOR(bit1, bit2):
    if bit1 == bit2:
        return "0"
    else:
        return "1"

def XORonByte(byte, key):
    result = ""
    i = 0
    while i < len(byte):
        result += XOR(byte[i], key[i])
        i += 1
    return result
    
print(XORonByte("00011000","10010010"))

def XORonLetter(letter, keyLetter):
    letterBin = encode(letter)
    keyLetterBin = encode(keyLetter)

    encryptedLetter = XORonByte(letterBin, keyLetterBin)

    return decode(encryptedLetter)

def XORonSentence(sentence, key):
    encryptedSentence = ""
    i = 0
    j = 0
    while i < len(sentence):
        if i-j >= len(key):
            j += len(key)
        encryptedSentence += XORonLetter(sentence[i], key[i-j])
        i += 1
    return encryptedSentence

## Function below is not used, I did the "j" method
def generateKey(message, key):
    if len(message) == len(key):
        return key
    elif len(message) < len(key):
        return key[p:len(message)]
    else:
        rem = len(message)%len(key)
        repetitions = math.floor(len(message)/len(key))
        tempKey = ""
        
        i = 0
        while i < repetitions:
            tempKey += key
            i += 1
        tempKey += key[0:rem]
        return tempKey

msg = input("What will be your encoded message?")
k = input("What is your key for this message?")
print("Your encoded message is: " + XORonSentence(msg, k))