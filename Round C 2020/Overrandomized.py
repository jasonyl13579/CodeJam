# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:14:31 2020

@author: Corn
"""
import collections
def solver(u):
    num = collections.defaultdict(int)
    ch = set()
    for i in range(10000):
        n, r = input().split()
        num[r[0]] += 1
        ch.add(r[-1])
    
    s = ''.join([k for k, v in sorted(num.items(), key=lambda x:x[1], reverse=True)])
    for c in s:
        ch.remove(c)
    return ch.pop() + s
T = int(input())
for case in range(T):
    u = int(input())
    print ('Case #{}: {}'.format(case+1, solver(u)))