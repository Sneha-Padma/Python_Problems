#Day18 Subset sum problem
def subset_sum(n, S, arr):
    dp = [False] * (S + 1)
    dp[0] = True  
    for a in arr:
        for x in range(S, a - 1, -1):
            if dp[x - a]:
                dp[x] = True
    
    return "YES" if dp[S] else "NO"

n, S = map(int, input().split())
arr = list(map(int, input().split()))
print(subset_sum(n, S, arr))
