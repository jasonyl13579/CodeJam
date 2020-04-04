# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:50:51 2020

@author: Corn
"""


def solver(A):
    res = ['C'] * len(A) 
    C_end = 0
    J_end = 0
    time = sorted(A, key = lambda x: (x[1], x[2]))
    #print (time)
    for i, st, et in time:
        if st < C_end and st < J_end: return "IMPOSSIBLE"
        if st >= C_end:
            res[i] = "C"
            C_end = et
        else:
            res[i] = "J"
            J_end = et
    return ''.join(res)
    
T = int(input())
for case in range(T):
    N = int(input())
    A = []
    for i in range(N):  
        time = [i]
        for x in input().split():
            time.append(int(x))
        A.append(time)
    res = solver(A)
    print ("Case #{}: {}".format(case+1, res))