
dict = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 
        'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliet', 'K':'Kilo', 
        'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 
        'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 
        'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}

def to_nato(words, dict):
    code = []
    for c in words.split():
        print(words.split())
        for l in c:
            if l.upper() in dict: 
                code.append(dict.get(l.upper()))
                code.append(" ")
            else:
                code.append(l)
    return ''.join(code)

def to_nato_bis(words):
    return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')

code = to_nato(".?Dd?", dict)
print(code)

