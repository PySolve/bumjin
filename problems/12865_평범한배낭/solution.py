from sys import stdin as stdin   

N, MAXIMUM_VALUE = map(int, stdin.readline().strip().split())
dp = [0 for i in range(MAXIMUM_VALUE+1)]

weights = []
for i in range(N):
    weight, value = map(int,  stdin.readline().strip().split())
    dp[weight] = value  
    weights.append(weight)

weights.sort()
for i in weights:
    for j in weights:
        if i-j>0:
            dp[i] = max(dp[i], dp[j]+dp[i-j])

print(dp[MAXIMUM_VALUE])

