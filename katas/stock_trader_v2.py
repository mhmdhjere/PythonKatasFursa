def max_profit(prices):
    curr_buy_price = float('inf')
    curr_profit = 0

    for p in prices:
        if p < curr_buy_price:
            curr_buy_price = p
        elif p > curr_buy_price:
            curr_profit = curr_profit + p - curr_buy_price
            curr_buy_price = p
    return curr_profit


if __name__ == '__main__':
    stock_prices = [7, 1, 5, 3, 6, 4]
    profit = max_profit(stock_prices)
    print(f"Maximum Profit: {profit}")  # should be 7

    # Additional test cases
    prices1 = [1, 2, 3, 4, 5]
    print(f"Maximum Profit: {max_profit(prices1)}")  # should be 4

    prices2 = [7, 6, 4, 3, 1]
    print(f"Maximum Profit: {max_profit(prices2)}")  # should be 0
