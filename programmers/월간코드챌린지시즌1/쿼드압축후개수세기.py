def recursive(arr, i,j, size, count):
    if size==1:
        count[arr[i][j]] +=1
        return 
    
    start_value = arr[i][j]
    for r in range(size):
        for c in range(size):
            if arr[i+r][j+c] != start_value:
                drk = [0, size//2, 0,size//2]
                dck = [0, 0, size//2,size//2]
                for k in range(4):
                    start_r, start_c = i+drk[k], j+dck[k]
                    recursive(arr, start_r, start_c, size//2, count)
                return 
    count[start_value] +=1 
    

def solution(arr):
    count = [0,0]
    recursive(arr, 0,0, len(arr), count)
    return count


import unittest

class SolutionTest(unittest.TestCase):
    def setUp(self):
        pass 

    def tearDown(self):
        pass 

    def test1(self):
        self.assertEqual(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]), [4,9])
        self.assertEqual(solution(  [[1,1,1,1,1,1,1,1],
                                        [0,1,1,1,1,1,1,1],
                                        [0,0,0,0,1,1,1,1],
                                        [0,1,0,0,1,1,1,1],
                                        [0,0,0,0,0,0,1,1],
                                        [0,0,0,0,0,0,0,1],
                                        [0,0,0,0,1,0,0,1],
                                        [0,0,0,0,1,1,1,1]]),
                                    [10,15])


if __name__ == '__main__':
    unittest.main()