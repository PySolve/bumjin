# ==================================
# Solution of the DP problem (신나는 함수 실행)
# https://www.acmicpc.net/problem/9184
#===================================

dp = [[[-1 for i in range(51)] for j in range(51)] for k in range(51)]
    
def topdown(a,b,c):
    # === Basis ===    
    if a <= 0 or b <= 0 or c <= 0: 
        return 1
    elif a > 20 or b > 20 or c > 20:
        return topdown(20,20,20)

    elif dp[a][b][c] != -1:
        return dp[a][b][c]
    
    # === Recursive ===
    else:
        if a < b and b < c:
            dp[a][b][c] = (topdown(a,b,c-1)
                                + topdown(a,b-1, c-1)
                                - topdown(a,b-1,c))
        else:
            dp[a][b][c] = (topdown(a-1,b,c) 
                                + topdown(a-1, b-1, c)
                                + topdown(a-1, b, c-1)
                                - topdown(a-1, b-1, c-1))
        return dp[a][b][c]


import sys 
while 1: 
    a,b,c = map(int, sys.stdin.readline()
                                .strip()
                                .split())
    if a==-1 and b==-1 and c==-1:
        break 
    print(f"w({a}, {b}, {c}) = {topdown(a,b,c)}")