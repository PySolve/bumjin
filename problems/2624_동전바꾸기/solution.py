import sys 
sys.setrecursionlimit(150000)
T = int(input()) # Target Number
K = int(input()) # Number of coins
coins = [list(map(int, input().split())) for k in range(K)] # coin value, limit


# === initialize dp ===
dp = [[0 for i in range(T+1)] for j in range(2)]

step = coins[0][0]
for i in range(1, coins[0][1]+1):
    if i*step<=T:
        dp[0][i*step] = 1 

for c in range(1, K):
    prev, curr = (c+1)%2, c%2
    step = coins[c][0]
    for i in range(1, coins[c][1]+1):
        for k in range(T+1):
            if k+i*step<=T:
                dp[curr][k+i*step] += 1+dp[prev][k] 
print(dp[curr])