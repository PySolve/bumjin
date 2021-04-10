N = int(input())

dp = [1 for i in range(10)]
temp = dp[:]

for i in range(N-1):
    for j in range(1, 10):
        temp[j] = sum(dp[:j+1])
    for j in range(10):
        dp[j] = temp[j]    

print(sum(dp)%10007)