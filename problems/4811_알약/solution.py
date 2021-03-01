import math 

while True :
    n = int(input())
    if n==0:
        break 
    numerator = math.factorial(2*n)
    denominator = (n+1)* math.factorial(n)**2 
    print(numerator//denominator)