```python
def solution(priorities, location):
    answer = 0 
    indexes = [i for i in range(len(priorities))]
    
    for i in range(len(priorities)):
        answer += 1
        max_index = priorities.index(max(priorities))
        if indexes[max_index] == location:
            break
        # MAX를 제외하고 앞뒤로 순서를 바꿔준다. 
        priorities = priorities[max_index+1:] + priorities[:max_index]
        indexes = indexes[max_index+1:] + indexes[:max_index]    

    return answer

```
 
## References 
[1] Problem Link https://programmers.co.kr/learn/courses/30/lessons/42587
