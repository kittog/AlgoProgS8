# character w longest consecutive repetition

def test(word):
    c = 1
    l = []
    r = []
    for i in range(len(word) - 1):
        t = word[i]
        if word[i] == word[i+1]:
            c += 1
        else:
            l.append(word[i])
            r.append(c)
            c = 1
    print(t)
    l.append(t)
    r.append(c)

    i = r.index(max(r)) # max value
    t = (l[i], r[i])
    return t
