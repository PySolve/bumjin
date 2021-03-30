n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x]==x:
        return parent[x]
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x, y = find(x), find(y)
    if x < y :
        parent[y] = x
    elif x > y:
        parent[x] = y

import sys 
sys.setrecursionlimit(1000000)
for i in range(m):
    op, a,b  = map(int, sys.stdin.readline().strip().split())
    if op==1:
        if find(a)==find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)