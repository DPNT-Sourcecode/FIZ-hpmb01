from solutions.SUM import sum_solution
import unittest
from lib.solutions.sum.sum_solution import compute

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(compute(2,3),5)


if __name__ == '__main__':
    unittest.main()
