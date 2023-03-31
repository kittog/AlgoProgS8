# sum two arrays (str)
import numpy as np 

def sum_one(arr):
    sum_s = ""
    if len(arr) != 0:
        for i in range(len(arr)):
            sum_s += str(arr[i])
        return int(sum_s)
    else:
        return 0


def sum_arrays(array1,array2):
    # write your code here
    tot = sum_one(array1) + sum_one(array2)
    print(tot)
    tot_s = str(tot)
    a_sum = []
    if tot == 0 and np.sum(len(array1), len(array2)) == 0:
        return []
    else:
        if tot_s[0] == "-":
            a_sum.append(int(tot_s[:2]))
        for i in range(len(a_sum),len(tot_s)):
            a_sum.append(int(tot_s[i]))
        return a_sum