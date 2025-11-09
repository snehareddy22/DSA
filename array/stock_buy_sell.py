#Stock Buy And Sell
#brute force
def maxProfit(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n):           # Buy day
        for j in range(i + 1, n):  # Sell day
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit
# TC = O(n²)
# SC = O(1)

#optimal uisng kadanes algo
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for i in prices:
        min_price = min(min_price, i)      # keep track of lowest buy price
        profit = i - min_price             # potential profit if sold today
        max_profit = max(max_profit, profit)   # update max profit
    return max_profit
# TC = O(n)
# SC = O(1)

#dry run
'''
prices = [7, 1, 5, 3, 6, 4]
min_price = ∞,   max_profit = 0
Day 1: price=7 → min_price=7, profit=0
Day 2: price=1 → min_price=1, profit=0
Day 3: price=5 → profit=5-1=4 → max_profit=4
Day 4: price=3 → profit=3-1=2 → max_profit=4
Day 5: price=6 → profit=6-1=5 → max_profit=5
Day 6: price=4 → profit=4-1=3 → max_profit=5
output: 5
'''