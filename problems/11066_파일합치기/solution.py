

import math
def solution(lst):
    N = len(lst)
    weight =[[0 for i in range(N)] for j in range(N)]
    dp = [[math.inf for i in range(N)] for j in range(N)]
    for i in range(N):
        dp[i][i] = lst[i]
        for j in range(N):
            if abs(i-j) ==1:
                dp[i][j] = 2*(lst[i] + lst[j])

    for i in range(N):
        for j in range(i):
            if weight[0][j-1] ==0:
                weight[0][j-1] = sum(lst[0:j])
            if weight[j+1][i-1] ==0:
                weight[j+1][i-1] = sum(lst[j+1:i])
            dp[j][i] = min(dp[j][i], (
                                    dp[0][j-1]
                                    + dp[j+1][i] 
                                    + 2 * weight[0][j-1]
                                    + 2 * lst[j]
                                    + 2 * weight[j+1][i] 
                                    + 2 * lst[i]
                                    )
                        )       
    print(lst)
    for w in weight:
        print(w)
    print("------")
    for v in dp:
        print(v)
    return dp[0][-1]
      

import unittest 
class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([40,30,30,50]), 300)
        self.assertEqual(solution(list(map(int, 
                            "1 21 3 4 5 35 5 4 3 5 98 21 14 17 32".split())
                            )), 864)


if __name__ == "__main__":
    unittest.main()