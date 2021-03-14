
def top_down(n):
    if dp_TopDown[n]!=0:
        return dp_TopDown[n]
    possible = []
    for weight, value in weight_value_lst:
        if n-weight>=0:
            possible.append(dp_TopDown[n-weight]+value)
    dp_TopDown[n]=max(possible)
    return dp_TopDown[n]

def bottom_up():
    for weight, value in weight_value_lst:
        temp = dp_BottomUp[:]
        for j in range(weight, len(dp_BottomUp)):
            dp_BottomUp[j] = max(temp[j],temp[j-weight]+value)
    
    return dp_BottomUp


N, MAX_weight = map(int, input().split())
weight_value_lst = [list(map(int, input().split())) for i in range(N)]
weight_value_lst.sort()
weight_value_lst_revsere = sorted(weight_value_lst, reverse=True)

dp_TopDown = [0 for i in range(MAX_weight+1)]
dp_BottomUp = [0 for i in range(MAX_weight+1)]

for weight, value in weight_value_lst:
    dp_TopDown[weight] = max(dp_TopDown[weight], value)

top_down(MAX_weight)
bottom_up()
print(dp_TopDown)
print(dp_BottomUp)