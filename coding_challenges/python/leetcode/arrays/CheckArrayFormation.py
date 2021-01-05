'''
You are given an array of distinct integers arr and an array of integer arrays pieces,
where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order.
However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Constraints:

1 <= pieces.length <= arr.length <= 100
sum(pieces[i].length) == arr.length
1 <= pieces[i].length <= arr.length
1 <= arr[i], pieces[i][j] <= 100
The integers in arr are distinct.
The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).

'''

import itertools
import numpy as np

def canFormArrayBruteForce(arr, pieces):
    """
    :type arr: List[int]
    :type pieces: List[List[int]]
    :rtype: bool
    """
    l = list(range(0, len(pieces)))
    all_perms = list(itertools.permutations(l, len(pieces)))
    for p in all_perms:
        c_arr = []
        for i in p:
            c_arr = c_arr + pieces[i]
        if (c_arr == arr):
            return True
    return False

def canFormArray(inparr, pieces):
    """
    :type arr: List[int]
    :type pieces: List[List[int]]
    :rtype: bool
    """
    arr = inparr.copy()

    def find(item, pieces):
        for j in range(0, len(pieces)):
            if item in pieces[j]:
                return j
        return None

    def check_seq(arr):
        for i in range(1,len(arr)):
            if arr[i-1]-arr[i]!=-1:
                return False
        return True

    for f in arr:
        # find f in the pieces
        j = find(f, pieces)
        # get those elements out of the array
        if(j != None):
            to_pop = []
            for i in range(0,len(pieces[j])):
                for k in range(0, len(inparr)):
                    if(inparr[k] == pieces[j][i]):
                        to_pop.append(k)
            to_remove = []
            if(check_seq(to_pop)):
                for k in to_pop:
                    to_remove.append(inparr[k])
            arr = [x for x in arr if x not in to_remove]
    if(len(arr)==0):
        return True
    else:
        return False

