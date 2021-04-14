"""
https://js1jj2sk3.tistory.com/3
"""

import math

MAX = math.inf

def recur(x, y, cost, summ, dp):
    if dp[x][y] != MAX:
        pass 
    elif x == y :
        dp[x][y] =  0  
    elif x+1 ==y :
        dp[x][y] = cost[x] + cost[y]
    else:
        for mid in range(x, y):
            left = recur(x, mid, cost, summ, dp)
            right = recur(mid+1, y, cost, summ, dp)
            dp[x][y] = min(dp[x][y], left + right)
        dp[x][y] += summ[y] - summ[x]  + cost[x]
    return dp[x][y]

def solution(cost):
    N = len(cost)
    summ = [0 for i in range(N)]
    for i in range(N):
        summ[i] = summ[i-1] + cost[i]
    dp = [[math.inf for i in range(N)] for j in range(N)]

    return recur(0, N-1, cost, summ, dp)
    

import argparse 
import sys  
sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    

    parser = argparse.ArgumentParser()
    parser.add_argument("--unittest",  action='store_true')
    parser.add_argument("--acmic", action='store_true')
    args = parser.parse_args()

    if args.acmic:
        T = int(input())
        for i in range(T):
            N = int(input())
            cost = list(map(int, input().split()))
            print(solution(cost))

    if args.unittest:
        while len(sys.argv)>1:
            sys.argv.pop() # remove flag
        import unittest 
        class SolutionTest(unittest.TestCase):
            def test(self):
                self.assertEqual(solution([40,30,30,50]), 300)
                self.assertEqual(solution(list(map(int, 
                                    "1 21 3 4 5 35 5 4 3 5 98 21 14 17 32".split())
                                    )), 864)
        unittest.main()