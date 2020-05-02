# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:52:25 2020

@author: Corn
"""
import collections
def solver(n, d, A):
    c = collections.Counter(A)
    #print (c)
    #k for k, v in sorted(num.items(), key=lambda x:x[1], reverse=True)
    for k, v in sorted(c.items(), key=lambda x:x[1], reverse=True):
        #print ("hi")
        #print (k,v)
        if v >= d: return 0
        if d == 2: return 1
        if d == 3:
            if v == 2 or k*2 in A: return 1
    return 2
T = int(input())
for case in range(T):
    n, d = input().split()
    A = [int(i) for i in input().split()]
    print ('Case #{}: {}'.format(case+1, solver(n, int(d), A)))
