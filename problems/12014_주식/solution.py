import sys 
input = sys.stdin.readline


def solve(lst, K, case):
    dp = [0]
    for i in lst:
        if i > dp[-1]:
            dp.append(i)
        else:
            left, right = 0, len(dp)-1
            while dp[left] < i:
                mid = (left + right)//2
                if dp[mid] < i :
                    left = mid + 1
                else:
                    right = mid - 1
            dp[left] = min(dp[left], i)
        if len(dp)-1 == K:
            print(f"Case #{case}")
            print(1)
            return 
    print(f"Case #{case}")
    print(0)
    
    

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    solve(lst, K, case=i+1)