def max_profit(prices):
    if not prices: 
        return 0
    
    buy_price = max(prices) + 1
    sell_price = 0
    curr_profit = 0
    for s in prices:
        if s < buy_price: 
            buy_price = s
        elif s >= sell_price:
            sell_price = s
            curr_profit = sell_price - buy_price if (sell_price - buy_price) > curr_profit else curr_profit

    return curr_profit


if __name__ == '__main__':
    stock_prices = [7, 1, 5, 3, 6, 4]
    profit = max_profit(stock_prices)
    print(f"Maximum Profit: {profit}")  # should be 5

    # Additional test cases
    prices1 = [7, 6, 4, 3, 1]
    print(f"Maximum Profit: {max_profit(prices1)}")  # should be 0 (no profit possible)

    prices2 = [1, 2, 3, 4, 5]
    print(f"Maximum Profit: {max_profit(prices2)}")  # should be 4 (buy at 1, sell at 5)