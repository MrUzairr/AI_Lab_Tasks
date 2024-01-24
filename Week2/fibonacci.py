def fibonacci(n):
    memo = {}

    memo[0] = 0
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]

n = int(input("Enter the term: "))
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
