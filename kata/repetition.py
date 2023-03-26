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

# suggestion (from codewars)
def longest_repetition(chars):
    max_char, max_count = '', 0
    char, count = '', 0
    for c in chars:
        if c != char:
            count, char = 0, c
        count += 1
        if count > max_count:
            max_char, max_count = char, count
    return max_char, max_count