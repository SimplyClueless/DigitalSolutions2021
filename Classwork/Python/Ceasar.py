def salad(word, shift):
    import string; return word.translate(str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])).translate(str.maketrans(string.ascii_uppercase, string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]))
print(salad(input("Enter text to be encrypted: "), int(input("Enter amount to shift characters by: "))))