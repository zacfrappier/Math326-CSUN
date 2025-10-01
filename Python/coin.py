def greedy_coin_change(coins, amount): #ChatGPT
    coins = sorted(coins, reverse=True)  # largest first
    res = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            res.append(coin)
    return res


def dp_coin_change(coins, amount):
    # DP array: min number of coins to make amount i
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    if dp[amount] == float("inf"):
        return []  # no solution

    # reconstruct solution
    res = []
    cur = amount
    while cur > 0:
        res.append(parent[cur])
        cur -= parent[cur]
    return res


# Example usage:
#coins = [1, 3, 4]
#amount = 6
coins = [11,10,1]
amount = 20
print("Greedy:", greedy_coin_change(coins, amount))
print("DP:", dp_coin_change(coins, amount))
