# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:56:25 2020

@author: Corn
"""

def solver(A, count):
    if not A: return ""
    x = min(A)
    i = A.index(x)
    add = x - count
    return "("* add + solver(A[0:i], x) + str(x) + solver(A[i+1:], x) + ")"* add
T = int(input())
for case in range(T):
    ans = solver([int(s) for s in input()], 0)
    print ('Case #{}: {}'.format(case+1, ans))