import sys 

def find(a):
    if a == parent[a]:
        return a 

    parent[a]= find(parent[a]) 
    return parent[a]


def union(a,b):
    setA, setB = find(a), find(b)
    if setA < setB :
        parent[setB] = setA
    else:
        parent[setA] = setB

input = sys.stdin.readline
V, E = map(int, input().strip().split())
parent = [i for i in range(V+1)]

lst = [ ]
for e in range(E):
    a, b, v = map(int, input().strip().split())
    lst.append((v,a,b))

lst.sort(key=lambda x : x[0])

total = 0
for v, a, b in lst:
    if find(a) != find(b):
        total += v 
        union(a,b)

print(total)
        