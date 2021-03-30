def run(num_zeros, base, N, robots, duration):
    # === 1. move belt ===
    out_base = (base+N-1)%(2*N) 
    robots[out_base] = 0 

    # === 2. move robots ===
    for i in range(2*N):
        current_pos = (base-i)%(2*N)
        if robots[current_pos]:
            next_pos = (base-i+1)%(2*N) 
            if (not robots[next_pos]) and duration[next_pos]>0:
                robots[current_pos] = 0
                robots[next_pos] = 1
                duration[next_pos] -=1 
                if duration[next_pos]==0:
                    num_zeros +=1 
    robots[out_base] = 0 
    
    # === 3. put robot ===
    if robots[base]==0 and duration[base]>0:
        robots[base] = 1
        duration[base] -=1
        if duration[base]==0:
            num_zeros +=1

    return num_zeros  


N, K = map(int, input().split())
duration = list(map(int, input().split()))
robots = [0 for i in range(2*N)] 
base = 0 
num_zeros = 0 
step = 0

# === run the conveyor belt ===
while num_zeros < K:
    step +=1 
    base = (base-1)%(N*2)
    num_zeros = run(num_zeros, base, N,  robots, duration)

print(step)
