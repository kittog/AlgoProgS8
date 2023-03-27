# chaser's schedule

import random as rd

#def solution(s, t):
    # s : speed
    # t : time
#    i, d = 0, 0 # index & distance
#    while i < t:
#        state = rd.choice([True, False])
#        if state == True:
#            s = s * 2
#        else:
#            s = (s - 1)
#        i += 1
#        d += s
#    return d

# generates sequence
def speed_sequence(t):
    seq = ""
    i = 1
    state = rd.choice(["S", "R"])
    while i <= t:
        seq += state   
        if state == "S":
            state = "R"
        else:
            state = rd.choice(["S", "R"])
        i += 1
    return seq

# find all sequences for given parameters
def max_speed(s, t):
    s = set()
    for i in range(500):
        s.add(speed_sequence(t))

    d = []
    for sequence in s:
        dist = 0
        for i in range(t):
            if sequence[i] == "S":
                dist += v * 2
            elif sequence[i] == "R":
                dist += v
            elif sequence[i] == "R" and sequence[i-1] == "S":
                v -= 1
        d.append(dist)

    return max(d)


# combine both
def solution(s, t):
    i = 0
    d = [] # distance list

    seqs = set()
    while i < 500: # tries
        dist = 0
        state = rd.choice(["S", "R"])
        seq = state
        for j in range(t - 1):
            if state == "S":
                dist += s * 2
                state = "R"
            elif state == "R":
                dist += s
                state = rd.choice(["R", "S"])
            elif state == "R" and seq[j-1] == "S":
                s -= 1
                dist += s
                state = rd.choice(["R", "S"])
            seq += state
        seqs.add(seq) # unique values
        d.append(dist)  # not matching values
        i += 1
    return max(d)
