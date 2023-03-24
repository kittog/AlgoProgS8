def is_isogram(string):
    #your code here
    s = string.lower()
    b = True
    for e in s:
        if s.count(e) > 1: 
            b = False
            break
    return b

def is_isogram_bis(string):
    return len(string) == len(set(string.lower()))

print(is_isogram("moOse"))

# set()
# set(str) returns set with all unique values/letters 
# in str element passed as input. ordered list.