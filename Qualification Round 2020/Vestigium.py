# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import collections
def countdup(l):
    c = collections.Counter(l)
   # print (c)
    for i in c:
        if c[i] > 1: return 1
    return 0
def solver(i, A):
    trace = colcount = rowcount = 0
    B = list(zip(*A))
    for x in range(len(A)):
        colcount += countdup(A[x])
        rowcount += countdup(B[x])
        for y in range(len(A[0])):
            if x == y: trace += A[x][y]
    print ("Case #{}: {} {} {}".format(i, trace,colcount,rowcount))
T = int(input())
for case in range(T):
    N = int(input())
    A = []
    for i in range(N):  
        A.append([int(x) for x in input().split()])
    solver(case, A)