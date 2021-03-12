n, m = map(int, input().split())
MAX = max(n, m)
dp = [[0 for i in range(MAX)] for j in range(MAX)]
for i in range(MAX):
    dp[0][i] =1 
    dp[i][0] =1 

for i in range(1, MAX):
    for j in range(1, i+1):
        dp[j][i-j] += dp[j-1][i-j] + dp[j][i-j-1]


for d in dp:
    print(d)

        
