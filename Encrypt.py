import json
import random 

class Encrypt:
    def __init__(self, key, message):
        self.key = key
        self.message = message

    def encrypt(self):
        # Load the emojies from local json list
        emojies = Encrypt.getEmojiList()
        self.shuffleEmojiList(emojies)
        print(emojies)
        maxEmojiNum = len(emojies) - 1

        messageSanitised = Encrypt.sanitise(self.message)

        
    # loads the emoji list from the json file 
    # 'emoji-list.json' included in the directory
    def getEmojiList():
        with open('emoji-list.json', 'r') as emojiFile:
            emojiObj = json.loads(emojiFile.read())

        return emojiObj['emojies']

    def shuffleEmojiList(self, emojies):
        # Random-Shuffle the list seeded with provided key
        randomKey = random.Random(self.key)
        randomKey.shuffle(emojies)

    def sanitise(message):
        #TODO: sanitising code for the message
        return message

    # Printing the emoji taking into consideration 
    # surrogate emojis. 
    def printEmoji(emoji):
        print(emoji.encode('utf-16','surrogatepass').decode('utf-16'))
        return None

e = Encrypt('hello', 'hello')
e.encrypt()

    