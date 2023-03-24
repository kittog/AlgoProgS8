# cryptage

def cryptage(s, l):
    cr = ""
    for car in s:
        cr += car
        for e, i in l:
            if car == e:
                cr = cr[:-1] + i
                break
    return cr

C = [("a","0"), ("c", "-"), ("d", "P"), ("e", "9"), ("i", "*"), ("s", "x"), (" ", "m"), ("u", " ")]
s = "le petit chat est mort"

print(cryptage(s, C))