import unittest
from katas.do_n_times import do_n_times

class FunctionCounter:
    def __init__(self):
        self.count = 0

    def inc_count(self):
        self.count += 1

class TestDoNTimes(unittest.TestCase):
    def test_do_n_times(self):
        obj = FunctionCounter()
        do_n_times(obj.inc_count, 3)
        self.assertEqual(obj.count, 3)
