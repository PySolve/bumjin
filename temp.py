b = int(input())

ten = 0 
for i in range(3):
    point = (b // (10 ** (i))) % 10 
    ten += point * 2 ** i

print("decimal=",ten)