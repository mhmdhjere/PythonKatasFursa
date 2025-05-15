import unittest
from katas.stock_trader_v2 import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_no_profit(self):
        self.assertEqual(max_profit([9, 8, 7, 6]), 0)
        self.assertEqual(max_profit([5, 5, 5, 5]), 0)

    def test_single_transaction(self):
        self.assertEqual(max_profit([1, 2, 3, 4]), 3)  # Buy at 1, sell at 4

    def test_multiple_transactions(self):
        self.assertEqual(max_profit([1, 5, 3, 6, 4, 8]), 11)  # (5-1) + (6-3) + (8-4)

    def test_peak_at_end(self):
        self.assertEqual(max_profit([2, 1, 4, 5, 7]), 6)  # Buy at 1, sell at 7

    def test_peak_at_start(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 7)  # (5-1) + (6-3)

    def test_empty(self):
        self.assertEqual(max_profit([]), 0)

    def test_single_price(self):
        self.assertEqual(max_profit([5]), 0)

    def test_two_prices(self):
        self.assertEqual(max_profit([5, 10]), 5)
        self.assertEqual(max_profit([10, 5]), 0)

if __name__ == "__main__":
    unittest.main()

