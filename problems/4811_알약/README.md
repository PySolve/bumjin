# 알약 

## 문제 

* `W`는 총 `N`개가 주어진다. 
* `H`는 총 `N`개가 주어진다. 
* 왼쪽 `W`의 개수는 `H`의 개수보다 많아야 한다. 



```python
import math 

while True :
    n = int(input())
    if n==0:
        break 
    numerator = math.factorial(2*n)            # W,H를 나열하는 모든 경우의 수
    denominator = (n+1)* math.factorial(n)**2  # W끼리 중복 / H끼리 중복 /  왼쪽 W개수가 더 많은 경우
    print(numerator//denominator)
```

## [Link](https://www.acmicpc.net/problem/4811)
