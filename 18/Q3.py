import unittest
from Q1 import ClockIterator  # Import the ClockIterator from Q1.py


class TestClockIterator(unittest.TestCase):
    def setUp(self):
        # Initialize a ClockIterator instance before each test
        self.clock_iterator = ClockIterator()

    def test_next_minute(self):
        # Test the __next__ method for the next minute
        # Assuming the iterator starts at "00:00"
        current_time = next(self.clock_iterator)  # This should now be "00:01"
        self.assertEqual(current_time, "00:01",
                         "The next minute should be 00:01.")

    def test_next_hour(self):
        # Test the __next__ method for hour increment
        for _ in range(59):  # Advance the iterator by one hour minus one minute
            next(self.clock_iterator)
        current_time = next(self.clock_iterator)  # This should be "01:00"
        self.assertEqual(current_time, "01:00",
                         "The next hour should be 01:00.")

    def test_midnight(self):
        # Test the __next__ method for midnight reset
        for _ in range(24 * 60 - 1):  # Advance the iterator by 24 hours minus one minute
            next(self.clock_iterator)
        current_time = next(self.clock_iterator)  # This should be "00:00"
        self.assertEqual(current_time, "00:00",
                         "The time should reset to 00:00 at midnight.")


# Running the tests
if __name__ == '__main__':
    unittest.main()
