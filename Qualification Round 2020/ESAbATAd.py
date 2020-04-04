# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 00:34:02 2020

@author: Corn
"""

def solver(b):
    ans = [0] * b
    q = 0
    for i in range(b+30):
        if q == b: break
        print (q+1, flush=True)
        r = int(input())
        if i % 10 != 0:
            ans[q] = r
            q += 1
    print (''.join([str(s) for s in ans]), flush=True)
T, b = [int(i) for i in input().split()] 
for case in range(T):
    solver(b)