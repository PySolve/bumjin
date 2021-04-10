class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def push(self, words):
        node = self.head

        for word in words:
            if word not in node.children.keys():
                node.children[word] = Node(word)
            node = node.children[word]

    def print(self, node, depth):
        keys = sorted(node.children.keys())
        for child in keys:
            print("--"*depth, end="")
            print(child)
            self.print(node.children[child], depth+1)

import sys 
input = sys.stdin.readline
N = int(input())

trie = Trie()
for i in range(N):
    lst = input().split()
    trie.push(lst[1:])
trie.print(trie.head, 0)



