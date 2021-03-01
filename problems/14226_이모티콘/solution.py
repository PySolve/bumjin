from collections import deque 

def bfs(target):
    queue = deque([(1,0,0)])
    visited = [False for i in range(target*2+1)]
    stacked = [False for i in range(target*2+1)]
    while True :
        value, clip, time = queue.popleft()
        visited[value] = True
        if value == target:
            return time 
        else:
            if value+clip<target*2 and not visited[value+clip] :
                queue.append((value+clip, clip, time+1))
            if not stacked[value]:
                queue.append((value, value, time+1))
                stacked[value] =True
            if value>1 and not visited[value-1]:
                queue.append((value-1, clip, time+1))

N = int(input())
print(bfs(N))


'''
## Base code. But OOM error
from collections import deque 

def bfs(target):
    queue = deque([(1,0,0)])
    visited = [False for i in range(target*2+1)]
    stacked = [False for i in range(target*2+1)]
    while True :
        value, clip, time = queue.popleft()
        if value == target:
            return time 
        else:
            queue.append((value+clip, clip, time+1))
            queue.append((value, value, time+1))
            queue.append((value-1, clip, time+1)
'''