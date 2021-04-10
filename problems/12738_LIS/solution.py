import sys 
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))

dp = [-10**20] 
for i in lst:
    if i > dp[-1]:
        dp.append(i)
    else:
        left, right = 0, len(dp)-1
        while dp[left] < i :
            mid = (left+right)//2
            if i > dp[mid]:
                left = mid + 1
            else:
                right = mid - 1
        dp[left] = min(dp[left], i)
    print(dp)
print(len(dp)-1)
