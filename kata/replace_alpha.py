# replace alpha

import string


def alphabet_position(text):
    text = text.lower()
    new = []
    alpha = list(string.ascii_lowercase)
    for i in range(len(text)):
        if text[i] in alpha:
            index = alpha.index(text[i])
            new.append(str(index + 1))
    return " ".join(new)
            

# solution kata bis
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

# ord : lowercase starts at 97 (hence the ord(c) - 96)