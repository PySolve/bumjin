

R, C, T = map(int, input().split())
import sys
import copy  
board1 = [list(map(int, sys.stdin.readline().split())) for i in range(R)]
board2 = copy.deepcopy(board1)


air_position = []
for i in range(R):
    for j in range(C):
        if board1[i][j] == -1:
            air_position.append([i,j])


dr = [0,0,1,-1]
dc = [1,-1, 0,0]

def spread(t):
    global R, C
    if t%2==0:
        board = board1
        other = board2 
    else:
        board = board2 
        other = board1 
    
    for i in range(R):
        for j in range(C):
            if other[i][j] != -1:
                other[i][j] = 0

    for i in range(R):
        for j in range(C):
            if board[i][j] != -1:
                value = board[i][j]
                spread = value//5 
                spreaded = 0
                for d in range(4):
                    nr, nc = i + dr[d], j + dc[d]
                    if 0<= nr < R and 0 <= nc < C:
                        if other[nr][nc] != -1:
                            other[nr][nc] += spread 
                            spreaded += spread 
                other[i][j] += value - spreaded 
    return other 

def run_machine(board):
    x,y = air_position[0]
    for r in range(x-2,-1, -1):
        board[r+1][0] = board[r][0]
    for c in range(1, C):
        board[0][c-1] = board[0][c]
    for r in range(1, x+1):
        board[r-1][-1] =  board[r][-1]
    for c in range(C-2, 0, -1):
        board[x][c+1] = board[x][c]
    board[x][1] = 0 


    x,y  = air_position[1]
    for r in range(x+2, R):
        board[r-1][0] = board[r][0]
    for c in range(1, C):
        board[-1][c-1] =board[-1][c]
    for r in range(R-2, x-1, -1):
        board[r+1][-1] = board[r][-1]
    for c in range(C-2, 0, -1):
        board[x][c+1] = board[x][c]  
    board[x][1] = 0 

    return board


for i in range(T):
    board = spread(i)
    board = run_machine(board)



count = 0
for i in range(R):
    for j in range(C):
        if board[i][j]>0 : 
            count += board[i][j]

print(count)
