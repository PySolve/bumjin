import sys 

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    lst = [0]
    for j in range(N):
        n = int(sys.stdin.readline())
        if n > lst[-1]:
            lst.append(n)
        else:
            left, right = 0, len(lst)-1
            while left < right:
                mid = (left+right)//2
                if lst[mid] < n :
                    left = mid+1
                else:
                    right = mid-1
            lst[left] = n         
    print(len(lst)-1)
    print(lst)
