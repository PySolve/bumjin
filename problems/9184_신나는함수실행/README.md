# 신나는 함수 실행 


## Basis 

```python
if a<=0 or b<=0 or c<=0:
    return 1

if a>20 or b > 20 or c > 0:
    return w(a,b,c) 
```


## Optimal Substructure

재귀함수 w(a,b,c)의 값을 구하는 문제는 다음과 같은 Sub problem 들로 값을 구할 수 있다. 

```python
if a < b and b < c:
    w(a,b,c) = w(a,b,c-1) + w(a,b-1, c-1) - w(a,b-1,c)

else:
    w(a-1,b,c) + w(a-1, b-1, c) + w(a-1, b, c-1) -  w(a-1, b-1. c-1)

return dp[a][b][c]
```


## Overlapping SubProblems

하위 Problem은 오직 한 번만 풀면 되며, 새로운 문제를 생성하지 않는다.


