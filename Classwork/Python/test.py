def oldmate(rawtext, inp):
    output = []
    cryptText = []

    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    if inp in upper:
        move = upper.index(inp)
        move = int(move)

    elif inp in lower:
        move = lower.index(inp)
        move = int(move)

    for eachLetter in rawtext:
        if eachLetter in upper:
            place = upper.index(eachLetter)
            encrypting = (place + move) % 26
            cryptText.append(encrypting)
            newLetter = upper[encrypting]
            output.append(newLetter)
        elif eachLetter in lower:
                place = lower.index(eachLetter)
                encrypting = (place + move) % 26
                cryptText.append(encrypting)
                newLetter = lower[encrypting]
                output.append(newLetter)
    return output

dude = oldmate(input("text for encryption: "), input("letter for encryption: "))
print(dude)