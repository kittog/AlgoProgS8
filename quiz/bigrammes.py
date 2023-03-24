# bigrammes

def bigramme(s):
    s_nouv = ""
    # liste id.
    for car in s:
        if car == " ": s_nouv += ""
        else:
            s_nouv += car
    # print
    print(s_nouv)
    for i in range(len(s_nouv)-1):
        print(s_nouv[i], s_nouv[i+1])

bigramme("la lune à Zanzibar")