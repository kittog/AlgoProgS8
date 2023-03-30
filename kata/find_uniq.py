# find unique number in array

import numpy as np

def find_uniq(arr):
    i = 0
    while i <= len(arr) and np.sum(arr == arr[i]) > 1:
        i += 1
    return arr[i]

# correction code wars
def find_uniq(arr):
    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e