"""
WH  1 

XXXX 2
XWXWXWX

WHWH  -->  W
WWHH

WHWHWH
WHWWHH

WWHHWH
WWWHHH

WWHH



"""

def construct_dp(n):
    count_lst = []





num_medicine_lst = []
while True:
    num_medicine = int(input())
    num_medicine_lst.append(num_medicine)
    if num_medicine==0:
        break 

count_lst = construct_dp(max(num_medicine_lst))
for num in num_medicine_lst:
    print(count_lst[num])