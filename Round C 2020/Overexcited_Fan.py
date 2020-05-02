# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:36:00 2020

@author: Corn
"""
import collections
def solver(x, y, m):
    visited = {}
    visited[(0,0)] = 0
    q = collections.deque()
    q.append((0,0))
    level = 0
    while level < len(m):
        if m[level] == 'N': y+=1
        if m[level] == 'W': x-=1
        if m[level] == 'E': x+=1
        if m[level] == 'S': y-=1
        level += 1
       # print (level, x, y)
        if abs(x)+abs(y) <= level: return str(level)
        '''
        n = len(q)
        for i in range(n):
            (cx, cy) = q.popleft()
           # print (cx, cy)
            for (dx, dy) in [(0,1),(1,0),(-1,0),(0,-1)]:
                nx, ny = dx+cx, dy+cy
                #print (nx, ny)
                if (nx, ny) not in visited:
                    visited[(nx, ny)] = level
                    q.append((nx, ny))
        '''
        #print (visited)
        #print ("s")
        #if (x, y) in visited: return str(level)
    return "IMPOSSIBLE"
T = int(input())
for case in range(T):
    x, y, m = input().split()
    ans = solver(int(x), int(y), m) 
    print ('Case #{}: {}'.format(case+1, ans))
