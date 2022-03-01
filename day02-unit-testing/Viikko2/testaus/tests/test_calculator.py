
import unittest
from Viikko2.testaus.calculator import calculator

class TestCalculator(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calculator.plus(3, 5), 8)

if __name__ == '__main__':
    unittest.main()
