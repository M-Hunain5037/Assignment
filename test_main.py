import unittest
from main import process_numbers

class TestProcessNumbers(unittest.TestCase):
    def test_sum_greater_than_100(self):
        self.assertEqual(process_numbers(101, 1), 102)

    def test_sum_equals_100(self):
        self.assertEqual(process_numbers(50, 50), 2500)

    def test_sum_less_than_100(self):
        self.assertEqual(process_numbers(30, 20), 10)

    def test_same_numbers(self):
        self.assertEqual(process_numbers(30, 30), 0)

if __name__ == '__main__':
    unittest.main()