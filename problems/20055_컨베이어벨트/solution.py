
def first_step(base, robots, length):
    base =(base-1)%length
    if robots and  robots[0] == (base+length//2-1)%length:
        robots.popleft()
    return base

def second_step(robots, durability, base, length, num_zero_duration):
    if robots:
        for index, robot_pos in enumerate(robots):
            next_pos = (robot_pos+1) % length 
            if durability[next_pos]>0:                
                if (len(robots)==1 or(len(robots)>1 and next_pos != robots[index-1])): 
                    robots[index] = next_pos
                    durability[next_pos] -=1
                    if durability[next_pos]==0:
                        num_zero_duration+=1

    return num_zero_duration

# === put robot on the base ===
def third_step(robots, base, step, durability, length, num_zero_duration):
    if durability[base]>0:
        for robot_pos in robots:
            if robot_pos == base:
                return num_zero_duration
        
        robots.append(base)
        durability[base] -=1
        if durability[base]==0:
            num_zero_duration+=1
    return num_zero_duration
    

def fourth_step(K, num_zero_duration):
    if num_zero_duration< K:
        return False  
    else:
        return True



from collections import deque
def run(N, K):
    length = 2*N
    step = 1
    num_zero_duration = 0
    durability = list(map(int, input().strip().split()))
    robots = deque([]) # position, time
    base = 0
    while 1:
        print(durability, robots,  (base+length//2-1)%length)

        base = first_step(base, robots, length)
        num_zero_duration = second_step(robots, durability, base, length, num_zero_duration)
        num_zero_duration =third_step(robots, base, step, durability,  length, num_zero_duration)
        done = fourth_step(K, num_zero_duration)
        if done:
            break 
        step +=1
        
    print(step)


import sys 
N, K = map(int, sys.stdin.readline()
                        .strip()
                        .split())

run(N, K)