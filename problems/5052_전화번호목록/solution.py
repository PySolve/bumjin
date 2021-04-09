class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def push(self, words):
        exist = True 
        cur = self.head 
        for word in words:
            if word not in cur.children.keys():
                cur.children[word] = Node(word)
                exist = False 
            cur = cur.children[word]
        return exist 

import sys 

input = sys.stdin.readline
T = int(input())
for t in range(T):
    trie = Trie()
    N = int(input())
    phone_numbers =[]

    for i in range(N):
        phone_numbers.append(list(input().strip()))
    phone_numbers.sort(key=lambda x: -len(x))
    exist = False 
    for number in phone_numbers:
        exist = trie.push(number)
        if exist:
            print('NO')
            break
    if not exist:
        print("YES")