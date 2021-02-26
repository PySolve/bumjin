def construct_dp(current):
    current_count = min(store_dp[current])
    searchDouble, searchMinus = False, False
    if 0< current <= N:
        if store_dp[current*2][0]==MAX:
            searchDouble = True 
        store_dp[current*2][0] = min(store_dp[current][0], current_count+2)

        if store_dp[current-1][1]==MAX:
            searchMinus = True 
        store_dp[current-1][1] = min(store_dp[current-1][1], current_count+1)
        if searchDouble:
            construct_dp(current*2)
        if searchMinus:
            construct_dp(current-1)


N = int(input())
MAX = 10000
store_dp = [[MAX,MAX] for i in range(N*2+1)]
store_dp[1] = [0,0]
construct_dp(1)
print(min(store_dp[N]))
print(store_dp)