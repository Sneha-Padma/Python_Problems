#Day7 Merge Two Sorted Arrays
def merged_sorted_arr():
    n1 = int(input())
    arr1 = list(map(int,input().split()))
    n2= int(input())
    arr2 = list(map(int,input().split()))

    result= sorted(arr1 + arr2)
    print(*result)
merged_sorted_arr()