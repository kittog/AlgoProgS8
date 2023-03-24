# n-grammes

def ngrammes(l, n):
    for i in range(len(l)):
        s = ""
        for  c in range(n, len(l)-n):
            s += l[i + c]
        print(s)

c = "Natacha aime les pommes de terre".split()

ngrammes(c, 2)
