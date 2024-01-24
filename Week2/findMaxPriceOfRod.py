def findMax():
    price = [3, 5, 8, 9, 10, 17, 17, 20]
    n = len(price)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        maximum = 0
        for j in range(1, i + 1):
            if j <= 8:
                maximum = max(maximum, price[j - 1] + dp[i - j])
        dp[i] = maximum

    return dp[n]

result = findMax()
print("Maximum Sum is:", result)
