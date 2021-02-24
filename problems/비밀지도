```python
def solution(n, arr1, arr2):
    arr1 = [bin(i)[2:] for i in arr1]
    arr1 = ["0"*(n-len(i)) +i for i in arr1]
    
    arr2 = [bin(i)[2:] for i in arr2]
    arr2 = ["0"*(n-len(i)) +i for i in arr2]
    
    
    answer = []
    for i in range(n):
        answer.append([])
        for j in range(n):
            if arr1[i][j]=="1" or arr2[i][j]=="1":
                answer[i].append("#")
            else:
                answer[i].append(" ")
    answer = ["".join(i) for i in answer]
    return answer

```

## References 
[1] Problem Link https://programmers.co.kr/learn/courses/30/lessons/17681
