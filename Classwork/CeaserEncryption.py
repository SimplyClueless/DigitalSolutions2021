import string

def salad(word, shift): 
    shifted = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    return word.translate(shifted)

print(salad(input("Enter text to be encrypted: "), 5))