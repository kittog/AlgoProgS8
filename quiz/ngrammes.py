# n-grammes

def ngrammes(l, n):
    for i in range(len(l)):
        s = ""
        for  c in range(n, len(l)-n):
            s += l[i + c]
        print(s)

c = "Natacha aime les pommes de terre".split()

# solution de natacha
def ngramme(phrase, n):
    for i in range(len(phrase) - n + 1):
      
        print(phrase[i:i+n]) 