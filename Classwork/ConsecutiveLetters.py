def consecutiveLetters(word):
    for cycle in range(0, len(word), 1):
        if word[cycle-1:cycle] == word[cycle:cycle+1]: return True
    return False

print(consecutiveLetters(input("Enter a word: ")))