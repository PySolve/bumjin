def move_up(board, red, blue, hole):
    if red[0] <= blue[0]:
        first, second  = red, blue 
    else:
        first, second = blue, red 

    fixed = first[1] 
    for r in range(first[0]-1, -1, -1):
        if [r, fixed] == hole:
            first[0] = r
            break
        if [r, fixed] == second:
            break 
        if board[r][fixed] ==".":
            first[0] = r
        else:
            break

    fixed = second[1] 
    for r in range(second[0]-1, -1, -1):
        if [r, fixed] == hole:
            second[0] = r
            break
        if [r, fixed] == first:
            break 
        if board[r][fixed] ==".":
            second[0] = r
        else:
            break
    
    return red, blue


def move_down(board, red, blue, hole):
    if red[0] >= blue[0]:
        first, second  = red, blue 
    else:
        first, second = blue, red 

    fixed = first[1] 
    for r in range(first[0]+1, len(board)):
        if [r, fixed] == hole:
            first[0] = r
            break
        if [r, fixed] == second:
            break 
        if board[r][fixed] ==".":
            first[0] = r
        else:
            break

    fixed = second[1] 
    for r in range(second[0]+1, len(board)):
        if [r, fixed] == hole:
            second[0] = r
            break
        if [r, fixed] == first and [r, fixed] != hole:
            break 
        if board[r][fixed] ==".":
            second[0] = r
        else:
            break
    
    return red, blue

def move_right(board, red, blue, hole):
    if red[1] >= blue[1]:
        first, second  = red, blue 
    else:
        first, second = blue, red 

    fixed = first[0] 
    for c in range(first[1]+1, len(board[0])):
        if [fixed, c] == hole:
            first[1] = c
            break
        if [fixed, c] == second:
            break 
        if board[fixed][c] ==".":
            first[1] = c
        else:
            break

    fixed = second[0] 
    for c in range(second[1]+1, len(board[0])):
        if [fixed, c] == hole:
            second[1] = c
            break
        if [fixed, c] == first:
            break 
        if board[fixed][c] ==".":
            second[1] = c
        else:
            break
    
    return red, blue


def move_left(board, red, blue, hole):
    first, second = None, None 
    if red[1] <= blue[1]:
        first, second  = red, blue 
    else:
        first, second = blue, red 

    fixed = first[0] 
    for c in range(first[1]-1, -1, -1):
        if [fixed, c] == hole:
            first[1] = c
            break
        if [fixed, c] == second:
            break 
        if board[fixed][c] ==".":
            first[1] = c
        else:
            break

    fixed = second[0] 
    for c in range(second[1]-1,-1, -1):
        if [fixed, c] == hole:
            second[1] = c
            break
        if [fixed, c] == first:
            break 
        if board[fixed][c] ==".":
            second[1] = c        
        else:
            break
    
    return red, blue


import sys 
from collections import deque 

functions = [move_up, move_down, move_left, move_right]

def bfs(board, red, blue, hole):
    queue = deque([[red, blue, 0, "None"]])
    while queue : 
        red, blue, count, name = queue.popleft()
        for func in functions:
            if name != func.__name__:
                red_t, blue_t = func(board, red[:], blue[:], hole)
                if hole == blue_t or hole== red_t:
                    if hole != blue_t:
                        return count+1
                elif count<9:
                    queue.append([red_t, blue_t, count+1, func.__name__])

    return -1


if __name__ == "__main__":
    M, N = map(int, input().split())
    board = [list(sys.stdin.readline().strip()) for i in range(M)]
    # === extract ball position in the board and replace it with `.` ===
    for r in range(M): 
        for c in range(N):
            if board[r][c] == "R":
                red = [r,c]
                board[r][c] = "."
            elif board[r][c] =="B":
                blue = [r,c]
                board[r][c] = "."
            elif board[r][c] == "O":
                hole = [r,c] 


    count = bfs(board, red, blue, hole)
    print(count)