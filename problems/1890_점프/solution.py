import sys 
sys.setrecursionlimit(10000000)

def topdown_dp(r,c):
    if dp[r][c] !=0:
        return dp[r][c]
    else:
        row_dp = [0]
        col_dp = [0]        
        for i in range(r):
            if board[i][c]+i ==r:
                row_dp.append(topdown_dp(i,c))
        for j in range(c):
            if board[r][j]+j ==c:
                col_dp.append(topdown_dp(r,j))
        dp[r][c] = sum(row_dp) + sum(col_dp) 
        return dp[r][c]

N = int(input())
board = [list(map(int, input().split())) for i in range(N)]
dp = [[0 for i in range(N)] for j in range(N)]
dp[0][0] = 1
topdown_dp(N-1, N-1)
print(dp[N-1][N-1])