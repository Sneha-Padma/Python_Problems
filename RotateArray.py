# Day10 Rotate an Array by k Positions
n, k = map(int, input().split())
arr = list(map(int, input().split()))
k = k % n  
rotated = arr[-k:] + arr[:-k] if k != 0 else arr
print(*rotated)
