num_cards = int(input())
prices = list(map(int, input().split()))

max_store_by_num = [p for p in prices]  # 0 index is 1 number of card
for i in range(1, num_cards):
    for j in range(0, i):
        partA, partB = max_store_by_num[j], max_store_by_num[i-j-1]
        max_store_by_num[i] = max(max_store_by_num[i], partA+partB)
print(max_store_by_num[-1])
