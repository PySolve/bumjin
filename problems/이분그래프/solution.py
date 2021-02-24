import sys 

def canBisect(graph, graph_linear, n):
    colors = [0 for i in range(n)]
    for v in range(n):
        if colors[v]==0:
            queue = [v]
            colors[v] = 1
            while queue:
                v = queue.pop(0)
                color = colors[v]
                for nei in graph[v]:
                    if colors[nei]==0:
                        colors[nei] = -color
                        queue.append(nei)

    for a,b in graph_linear:
        if colors[a] == colors[b]:
            return False
    return True

T = int(input())
for _ in range(T):
    v, e = map(int, map(int, sys.stdin.readline().strip().split()))
    graph = {i:[] for i in range(v)}
    graph_linear = []
    for i in range(e):
        a,b = map(int, map(int, sys.stdin.readline().strip().split()))
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
        graph_linear.append((a-1,b-1))
    if canBisect(graph, graph_linear, v):
        print("YES")
    else:
        print("NO")