#Day24 Maximum Subarray Sum with at Most K Deletions
def Subarray(n, K, A):
    dp = [-10**18]*(K+1)
    ans = -10**18
    for x in A:
        ndp = [-10**18]*(K+1)
        for j in range(K+1):
            ndp[j] = max(dp[j]+x, x)        
            if j>0: ndp[j] = max(ndp[j], dp[j-1])  
        dp = ndp
        ans = max(ans, max(dp))
    return ans
n,K = map(int,input().split())
A = list(map(int,input().split()))
print(Subarray(n,K,A))
