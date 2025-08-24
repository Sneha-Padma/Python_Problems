# Day6 Remove duplicate from an array
def remove_duplicate(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

n = int(input())
arr = list(map(int, input().split()))
unique_element = remove_duplicate(arr)
print(*unique_element)