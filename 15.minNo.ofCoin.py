#Day15 Minimum number of coins for a given amount
def coin_change_min(n, amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] = min(dp[x], 1 + dp[x - c])
    return dp[amount] if dp[amount] != float('inf') else -1
n, amount = map(int, input().split())
coins = list(map(int, input().split()))
print(coin_change_min(n, amount, coins))
