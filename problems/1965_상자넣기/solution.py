import sys 
N= int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range(1001)]
dp[lst[0]] = 1
for i in range(1, N):
    value = lst[i]
    maximum = 0
    for j in range(value-1, 0, -1):
        if dp[j] > maximum:
            maximum = dp[j]
    dp[value] = max(dp[value], maximum+1)
print(max(dp))