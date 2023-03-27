# doublons
def doublons(l):
    b = False
    for i in range(len(l) - 1):
        if l[i] == l[i+1]:
            b = True
    return b


# bonus
def uniq(l):
    # supprimer suites successives (réduites à une occurences)
    n = len(l)
    l_nouv = [l[0]]
    for i in range(1, n):
        print(l[i-1], l[i])
        if l[i-1] != l[i]:
            l_nouv.append(l[i])    
    return l_nouv


                    
# + simple : utiliser la fonction set()