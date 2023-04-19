def array_diff(a, b):
    # your code here
    for e in b:
        if e in b:
            i = a.index(e)
            a.pop(i)
    return a

def arr_diff(a, b):
    a_nouv = []
    for e in a:
        if e not in b:
            a_nouv.append(e)
    return a_nouv


#### CORRECTION CODEWARS
def array_diff(a, b):
    return [x for x in a if x not in b]

#### cube
def somme(n):
    s = 0
    for i in range(n+1):
        s += (n - i) ** 3
    return s

def cube(m):
    n = 1
    while somme(n) != m:
        n += 1
    return n

def fibo(n):
    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f