import string
import random

def oneTimePad(word):
    generatedPad = "".join(random.choice(string.ascii_lowercase) for x in range(len(word)))
    print(generatedPad)

    padConversion = str.maketrans(word, generatedPad)

    return word.translate(padConversion)

print(oneTimePad(input("Enter word: ")))