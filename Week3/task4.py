def min_coins(coins, target_amount):
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0

    for current_amount in range(1, target_amount + 1):
        for coin_value in coins:
            if current_amount >= coin_value:
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin_value] + 1)

    return dp[target_amount]

coin_denominations = [1, 2, 5, 10, 20]
target_amount = int(input("Enter the target amount: "))

min_coins_required = min_coins(coin_denominations, target_amount)
print("Minimum coins required to make change:", min_coins_required)
