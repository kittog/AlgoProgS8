# scoring word
import string

def high(x):
    alpha = list(string.ascii_lowercase)
    words = x.split()
    sum = []
    for w in words:
        s = 0
        for l in w:
            s += alpha.index(l) + 1
        sum.append(s)
        imax = sum.index(max(sum))
    return words[imax]  

# correction en une ligne made in codewars
def high_bis(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k)) 