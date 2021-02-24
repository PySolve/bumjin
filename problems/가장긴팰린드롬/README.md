```python
def solution(s):
    answer = 1
    for i in range(1, len(s)-1):
        for j in range(1, min(len(s)-i, i+1)):   
            if s[i-j:i] == s[i+1:i+j+1][::-1]:   # odd case :  s = "ababa"
                answer = max(answer, 1+2*j)
            if s[i-j:i+1] == s[i+1:i+j+2][::-1]: # even case : s = "abaaba"
                answer = max(answer, 2+2*j)
            
    return answer

```

## References 

[1] Problem link : https://programmers.co.kr/learn/courses/30/lessons/12904
