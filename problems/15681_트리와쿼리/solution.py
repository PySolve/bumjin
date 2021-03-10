from collections import deque 
import sys 
sys.setrecursionlimit(200000)

# === construct bidrectional graph ===
N, R, Q = map(int, input().split())
graph = {i:[] for i in range(1, N+1)}
for i in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


# === construct tree ===
tree = {i:[] for i in range(1, N+1)}
visited = [False for i in range(N+1)]
queue = deque([R])
while queue:
    node = queue.popleft()
    visited[node] = True
    for nei in graph[node]:
        if not visited[nei] :
            tree[node].append(nei)
            queue.append(nei)

# === construct dp ===
dp = [0 for i in range(N+1)]
def recursive_dp(node):
    if len(tree[node])==0:
        dp[node]=1
        return 1 
    if dp[node] !=0:
        return dp[node]
    cumm = 1
    for nei in tree[node]:
        cumm += recursive_dp(nei)
    dp[node] = cumm
    return cumm
recursive_dp(R)

# === run code ===

for _ in range(Q):
    q = int(sys.stdin.readline())
    print(dp[q])
