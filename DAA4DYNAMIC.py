#4. Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and
#bound strategy.
def knapsack_01(n, values, weights, W):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items
    selected_items = []
    i, w = n, W
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:  # Item was included
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[n][W], selected_items

# Take input from the user
n = int(input("Enter the number of items: "))
values = list(map(int, input("Enter the values of the items separated by space: ").split()))
weights = list(map(int, input("Enter the weights of the items separated by space: ").split()))
W = int(input("Enter the maximum capacity of the knapsack: "))

max_value, selected_items = knapsack_01(n, values, weights, W)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
