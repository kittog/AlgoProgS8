# kata du vendredi baby
import numpy as np 
def expanded_form(num):
    exp = []
    s = str(num)
    n = len(s)
    i = 0
    while i < n - 1:
        if s[i] != "0":
            exp.append(s[i] + "0" * len(s[i+1:]))
        i += 1 
    if s[-1] != "0": exp.append(s[-1])
    return " + ".join(exp)


def build_tower(n):
    t = [] # tower
    space = (n*2 - 1) // 2
    for i in np.arange(1, n * 2, 2):
        stars = "*" * i
        f = " " * space + stars + " " * space
        space -= 1
        t.append(f)
    return t

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).
def solution(t):
    s = 0
    i = 0
    while t > 0 and i < t:
        if i % 3 == 0 or i % 5 == 0:
            s += i
        i += 1
    return s

def order(sentence):
    ord = []
    n = len(sentence.split())
    for i in range(1, n+1):
        for w in sentence.split():
            if str(i) in w:
                ord.append(w)
    return " ".join(ord)

def order_bis(sentence):
    return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))