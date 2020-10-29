import unittest
from calculator import calculator

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, calculator)

    def test_add_from_csv(self):
        fl = self.calculator.read_csv("../src/CSV/uadd.csv")

        for var in range(len(fl)):
            self.calculator.__add__(fl[0][var], fl[1][var])
            self.assertEqual(self.calculator.result, fl[2][var])


    def test_subtraction(self):
        fl = self.calculator.read_csv("../src/CSV/Unit Test Subtraction.csv")

        for var in range(len(fl)):
            self.calculator.__sub__(fl[0][var], fl[1][var])
            self.assertEqual(self.calculator.result, fl[2][var]*-1)


    def test_multiplication(self):

        fl = self.calculator.read_csv("../src/CSV/Unit Test Multiplication.csv")

        for var in range(len(fl)):
            self.calculator.__mul__(fl[0][var], fl[1][var])
            self.assertEqual(self.calculator.result, fl[2][var])



    def test_division(self):
        fl = self.calculator.read_csv("../src/CSV/Unit Test Division.csv")

        for var in range(len(fl)):
            self.calculator.__div__(fl[1][var], fl[0][var])
            self.assertEqual(int(self.calculator.result),int(fl[2][var]))

    def test_square(self):
        fl = self.calculator.read_csv("../src/CSV/Unit Test Square.csv")

        for var in range(len(fl)):
            self.calculator.__square__(fl[0][var])
            self.assertEqual(self.calculator.result,fl[1][var])


    def test_squareRoot(self):
        fl = self.calculator.read_csv("../src/CSV/Unit Test Square Root.csv")
        for var in range(len(fl)):
            self.calculator.__squareRoot__(fl[0][var])
            self.assertEqual(int(self.calculator.result), int(fl[1][var]))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
