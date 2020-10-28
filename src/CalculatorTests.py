import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator= Calculator()
        self.assertIsInstance(calculator, Calculator)


    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()