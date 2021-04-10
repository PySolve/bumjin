def make_trinary(n):
    value = 1
    while value*3 <= n:
        value *=3
    string = []
    while n>0:
        multiplicity = n//value
        n -= multiplicity * value
        string.append(multiplicity)
        value //= 3
    while value>0:
        string.append(0)
        value //=3
    return string

def convert_3_to_10(string):
    n=0
    for i in range(len(string)):
        n += string[i]*3**i
    return n

def solution(n):
    
    string = make_trinary(n)
    answer = convert_3_to_10(string)
    return answer


import unittest

class SolutionTest(unittest.TestCase):
    def setup(self):
        pass 

    def tearDown(self):
        pass 

    def test(self):
        self.assertEqual(solution(45), 7)
        self.assertEqual(solution(125), 229)

if __name__ =="__main__":
    unittest.main()