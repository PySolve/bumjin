# === initialize dp ===
n, m = map(int, input().split())
dp = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    dp[i][0] =1
for i in range(n):
    dp[0][i] =1

# === fill the dp ===
from collections import deque
# fill the right side with bfs 
queue = deque([[r,1] for r in range(m) if n>1])
while queue:
    r,c =queue.popleft() 
    if r==0:
        dp[r][c] =  dp[r][c-1] 
    else:
        dp[r][c] = dp[r-1][c] + dp[r][c-1] + dp[r-1][c-1]
    if c+1<n:
        queue.append([r, c+1])

# === print the result ===
print(dp[m-1][n-1]%1000000007)