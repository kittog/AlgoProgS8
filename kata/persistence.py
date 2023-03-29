# produit des digits d'un nombre

def persistence(n):
    c = 0
    while len(str(n)) > 1:
        p = 1
        for i in str(n):
            p *= int(i)
        print(p)
        n = str(p)
        c += 1
    return c