def wave(people):
    l = []
    n = len(people)
    for i in range(n):
        if people[i] != " ":
            l.append(people[:i] + people[i].upper() + people[i+1:])
    return l
        


w = wave("muchacha muchacho")