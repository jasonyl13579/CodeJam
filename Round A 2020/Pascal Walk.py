# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 10:36:00 2020

@author: Corn
"""
pascal = [[0]*1001 for i in range(1001)]
pascal[0][0] = 1
for i in range(1, 1001):
    for j in range(1, 1001):
        pascal[i][j] =  pascal[i-1][j] + pascal[i-1][j-1]
    #if i < 10:
    #    print (pascal[i][0:10])

def dfs(n, path):
    (x, y) = path[-1]
    cand = []
    if pascal[x][y] == n : return True
    n -= pascal[x][y]
    for (dx, dy) in [(1,1),(0, 1),(-1,0),(1,0),(-1,0)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in path and nx >= ny and nx > 0 and ny > 0 and pascal[nx][ny] <= n:
            cand.append((pascal[nx][ny],nx,ny))
    cand = sorted(cand, reverse = True)
    #print (n)
    #print (cand)
    for val, i, j in cand:
        path.append((i,j))
        if dfs(n, path): return True
        path.pop()
T = int(input())
for case in range(T):
    n = int(input())
    path = [(1,1)]
    dfs(n, path)
    print ('Case #{}:'.format(case+1))
    for p in path:
        print (str(p[0]) + ' ' + str(p[1]))
