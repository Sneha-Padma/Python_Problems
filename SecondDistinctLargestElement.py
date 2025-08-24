#Day8 Second Distinct Larget Element in an Array
n = int(input())
arr = list(map(int, input().split()))
unique_elements = set(arr)
if len(unique_elements) < 2:
    print("NO")
else:
    sorted_unique = sorted(unique_elements, reverse=True)
    print(sorted_unique[1])
