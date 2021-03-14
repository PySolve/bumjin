class MyBitMask:
    def __init__(self):
        self.memory = 0

    def add(self, i):
        self.memory |= (1 << i)
    
    def remove(self, i):
        self.memory &=  ~(1 << i)

    def check(self, i):
        if (self.memory &( 1<< i)):
            print(1)
        else:
            print(0)

    def toggle(self, i):
        self.memory ^=(1<<i)
    
    def all(self):
        self.memory = (1<<21)-1
        
    def empty(self):
        self.memory = 0

my_set = MyBitMask()

import sys 
N = int(sys.stdin.readline().strip())
for i in range(N):
    command = sys.stdin.readline().strip().split()
    if len(command)==1:
        getattr(my_set, command[0])()
    else:
        getattr(my_set, command[0])(int(command[1]))
