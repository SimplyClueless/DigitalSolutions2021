import string
def salad(word, shift):
    lowerCharacterShift = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    upperCharacterShift = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift])
    return word.translate(lowerCharacterShift).translate(upperCharacterShift)
print(salad(input("Enter text to be encrypted: "), int(input("Enter amount to shift characters by: "))))