N = int(input())
S = 0 
count = 0
for i in range(1, N+1):
    S +=i
    if S>N:
        break
    count +=1 
print(count)