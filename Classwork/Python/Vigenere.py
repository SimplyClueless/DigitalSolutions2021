import string
def salad(word, shift): 
    while len(shift) < len(word):
        difference = 26 - len(shift)
        shift += shift[:difference]
        print(shift)
    characterShift = str.maketrans(string.ascii_lowercase, shift)
    return word.translate(characterShift)
print(salad(input("Enter text to be encrypted: "), input("Enter word to encrypt with: ")))