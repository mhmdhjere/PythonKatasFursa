import unittest
import time
from katas.time_me import measure_execution_time

def sample_function():
    """A function that sleeps for 500ms."""
    time.sleep(0.5)


def quick_function():
    """A function that performs a quick task."""
    print("Quick task done!")


class TestSumOfDigits(unittest.TestCase):
    # this test checks that the time is in reasonable range close to 500ms
    def test_time_me_half_second(self):
        t = measure_execution_time(sample_function)
        self.assertTrue(500 <= t <= 520, f"Expected ~500ms, got {t}ms")

    def test_time_me_one_ms(self):
        t = measure_execution_time(quick_function)
        self.assertTrue(t < 1, f"Expected < 1ms, got {t}ms")







