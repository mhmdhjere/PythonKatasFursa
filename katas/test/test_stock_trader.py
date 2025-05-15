import unittest
from katas.stock_trader import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_increasing_prices(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5]), 4)  # Buy at 1, sell at 5

    def test_decreasing_prices(self):
        self.assertEqual(max_profit([9, 8, 7, 6, 5]), 0)  # No profit possible

    def test_single_transaction_best_profit(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)  # Buy at 1, sell at 6

    def test_multiple_options_only_best_matters(self):
        self.assertEqual(max_profit([2, 4, 1, 7, 3, 6]), 6)  # Buy at 1, sell at 7

    def test_single_day(self):
        self.assertEqual(max_profit([5]), 0)

    def test_empty_list(self):
        self.assertEqual(max_profit([]), 0)

    def test_flat_prices(self):
        self.assertEqual(max_profit([3, 3, 3, 3]), 0)

    def test_profit_at_end(self):
        self.assertEqual(max_profit([5, 4, 3, 2, 1, 10]), 9)

    def test_profit_at_start(self):
        self.assertEqual(max_profit([1, 10, 5, 3]), 9)

if __name__ == "__main__":
    unittest.main()

