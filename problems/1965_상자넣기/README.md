#  상자 넣기 

## Overapping subproblems 



## Optimal Substructure


f(n)을 n 번째 상자가 주어졌을 때까지 한 번에 넣을 수 있는 최대 상자 개수라고 하자. 
w(n)은 n 번째 상자의 무게라고 하자. 

```
f(n+1) = f(w(n+1)) + 1
```

N 번째 상자가 주어진다면, N보다 작으면서 가장 큰 상자에서 1을 더한 값이 

f(N) = 