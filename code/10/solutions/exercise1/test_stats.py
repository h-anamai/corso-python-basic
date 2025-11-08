import unittest
from stats.stats import calculate_average

class TestStats(unittest.TestCase):

    def test_average_on_ints(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)

    def test_average_on_floats(self):
        self.assertEqual(calculate_average([1.5, 2.5, 3.5]), 2.5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_list_with_single_element(self):
        self.assertEqual(calculate_average([10]), 10.0)

if __name__ == '__main__':
    unittest.main()