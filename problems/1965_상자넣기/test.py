import sys 
input = sys.stdin.readline 
n = int(input()) 
box = list(map(int, input().split())) 
dp = [0]*n 
dp[0] = 1 
for i in range(1, n):
    max_size = dp[i] 
    index = i #box[i]보다 작은 크기의 상자가 있었는지 체크하는 변수 
    for j in range(i): 
        if box[j]<box[i] and max_size<dp[j]: #box[i]보다 작으면서 dp 값이 제일 큰 인덱스를 찾으려는 for문 
            max_size = dp[j] 
            index = j #작은 크기의 상자가 있었기때문에 index 값은 i가 아닌 값으로 바뀐다. 
    if index != i: #작은 크기의 상자가 있었으면 그 중 최댓값 + 1 
        if box[index] != box[i]: #이거는 없어도 맞긴 한데, 없으면 시간이 더 소요된다.. 왜 ?.. 
            dp[i] = max_size+1 
    else: #작은 크기의 상자가 없었다면 1대입 
        dp[i] = 1 
print(max(dp))
