# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 08:56:44 2020

@author: Corn
"""
def compare(ss):
    if len(ss) == 0: return ''
    ss = sorted(list(ss), key = lambda x: -len(x))
    #print (ss)
    for i in range(1, len(ss)):
        for j in range(len(ss[i])):
            if ss[i][j] != ss[0][j]: return '*'
    return ss[0]
def solver(ss):
    left = set()
    right = set()
    for s in ss:
        subs = s.split('*')
        if subs[0] != '': left.add(subs[0])
        if subs[-1] != '': right.add(subs[-1][::-1])
    ls, rs = compare(left), compare(right)[::-1]
    if ls == '*' or rs == '*': return '*'
    else: return ls + rs
T = int(input())
for case in range(T):
    n = int(input())
    ss = []
    for i in range(n):
        ss.append(input())
    ans = solver(ss)
    print ('Case #{}: {}'.format(case+1, ans))