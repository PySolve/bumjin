# === define bitmask operation class===
class MyBitMask:
    def __init__(self):
        self.memory = 0

    # === set 1 ===
    def add(self, i):
        self.memory |= (1 << i)
    
    # === set 0 ===
    def remove(self, i):
        self.memory &=  ~(1 << i)

    def check(self, i):
        if (self.memory &( 1<< i)):
            print(1)
        else:
            print(0)

    # === reverse(xor) ===
    def toggle(self, i):
        self.memory ^=(1<<i)
    
    # === 11111 11111 11111 11111 ===
    def all(self):
        self.memory = (1<<21)-1
        
    # === 00000 00000 00000 00000 ===    
    def empty(self):
        self.memory = 0

bitmask_handler = MyBitMask()

# === commands ===
import sys 
N = int(sys.stdin.readline().strip())
for i in range(N):
    command = sys.stdin.readline().strip().split()
    if len(command)==1:
        getattr(bitmask_handler, command[0])()
    else:
        getattr(bitmask_handler, command[0])(int(command[1]))