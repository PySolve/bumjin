"""
Consider the following case. 
XX8
XX9
XX0
XX1
XX2
XX3
XX4
XX5
XX6
XX7
"""
def construct_dp(n):
    store_count = [[1 for i in range(10)]]
    for i in range(1,n):
        count_per_digit = [0 for i in range(10)]
        for digit in range(0, 10):
            count_per_digit[digit] = sum(store_count[i-1][:digit+1])
        store_count.append(count_per_digit)
    return store_count

num_test_case = int(input())
targets = [int(input()) for i in range(num_test_case)]
stored_counts = construct_dp(max(targets))

for number in targets:
    print(sum(stored_counts[number-1]))