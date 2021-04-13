import bisect
def solution(lst):
    dp = [0]
    for i in lst:
        if i > dp[-1]:
            dp.append(i)
        position = bisect.bisect_left(dp, i)
        dp[position] = min(i, dp[position])
    return len(dp)-1


import unittest 
class SolutionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(solution([1,6,2,5,7,3,5,6]), 5)

if __name__ =="__main__":
    unittest.main()








"""
# Copy it for the ACMIC solution
import bisect
def solution(lst):
    dp = [0]
    for i in lst:
        if i > dp[-1]:
            dp.append(i)
        position = bisect.bisect_left(dp, i)
        dp[position] = min(i, dp[position])
    return len(dp)-1

def acmic_solution():
    import sys 
    N= int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    print(solution(lst))

acmic_solution()
"""
