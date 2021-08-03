import string
def salad(word, shift):
<<<<<<< HEAD
    import string
    lowerCharacters = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    upperCharacters = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift])
    return word.translate(lowerCharacters).translate(upperCharacters)
=======
    lowerCharacterShift = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    upperCharacterShift = str.maketrans(string.ascii_uppercase, string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift])
    return word.translate(lowerCharacterShift).translate(upperCharacterShift)
>>>>>>> ce03fa14f21a0bfd063df211ec57487c8033f4c2
print(salad(input("Enter text to be encrypted: "), int(input("Enter amount to shift characters by: "))))