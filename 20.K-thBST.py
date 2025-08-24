#Day20 K-th Smallest Element in a Binary Search Tree (BST)
import sys
sys.setrecursionlimit(200000) 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def kth_smallest(root, k):
    stack = []
    curr = root
    count = 0
    
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right
    
    return -1

n = int(sys.stdin.readline())
values = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

root = None
for v in values:
    root = insert(root, v)
print(kth_smallest(root, k))
