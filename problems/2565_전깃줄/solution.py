N = int(input())
lst = [list((map(int, input().strip().split()))) for i in range(N)]
lst.sort(key=lambda x:x[0])

def is_not_crossing(small,large):
    return lst[small][0] < lst[large][0] and lst[small][1] < lst[large][1]

dp = [0 for i in range(N)]
for current in range(N):
    max_dp = 0
    max_index = current
    for candi in range(current):
        # Cross 하지 않으면서 가장 큰 DP를 찾는다. 
        if dp[candi] > max_dp and is_not_crossing(candi, current):
            max_dp = dp[candi]
            max_index = candi
    dp[current] = dp[max_index]+1

print(N-max(dp))