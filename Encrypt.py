import json
import random 

class Encrypt:
    def __init__(self, key, message):
        # Store the key and message
        self.key = key
        self.message = message

        # Load the emojies from local json list
        self.emojis = Encrypt.getEmojiList()
        self.shuffleEmojiList(self.emojis)

        self.numEmojis = len(self.emojis)

    # Encrypt the message 
    def encrypt(self):

        bitString = self.stringToBits()
        numEmojisBitLength = len(format(self.numEmojis, '01b'))

        bitsArray = Encrypt.bitsArraySplit(bitString, numEmojisBitLength)

        emojiString = ''
        for bits in bitsArray:
            emojiString += self.bitsToEmoji(bits)

        return emojiString

    # Convert characters to bit Strings
    def stringToBits(self):
        bitString = ''
        for character in self.message:
            bitString += format(ord(character), '01b')

        return bitString

    # Convert bit string into an array of equal size
    # bit strings
    def bitsArraySplit(bitString, numEmojisBitLength):
        bitStart = 0
        bitEnd = numEmojisBitLength

        emojiBitsList = []
        while bitStart < bitEnd:
            emojiBitsList.append(bitString[bitStart:bitEnd])

            bitStart += numEmojisBitLength
            bitEnd += numEmojisBitLength

            if bitEnd > len(bitString):
                bitEnd = len(bitString)

        return emojiBitsList

    # Convert bit strings into an index
    # Map the string to emoji in json
    def bitsToEmoji(self, bits):
        if not bits:
            return 

        index = int(bits, 2) % len(self.emojis)

        return self.emojis[index] 
        
    # loads the emoji list from the json file 
    # 'emoji-list.json' included in the directory
    def getEmojiList():
        with open('emoji-list.json', 'r') as emojiFile:
            emojiObj = json.loads(emojiFile.read())

        return emojiObj['emojies']

    # shuffle the emoji list randomly
    # use the key provided as the seed for consistent shuffle
    def shuffleEmojiList(self, emojies):
        # Random-Shuffle the list seeded with provided key
        randomKey = random.Random(self.key)
        randomKey.shuffle(emojies)

    # Printing the emoji taking into consideration 
    # surrogate emojis. 
    def printEmoji(emoji):
        print(emoji.encode('utf-16','surrogatepass').decode('utf-16'))
        return None

message = input('Enter A Message : ')
key = input('Enter A Key : ')
e = Encrypt(key, message)
Encrypt.printEmoji(e.encrypt())

    