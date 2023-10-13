import unittest
from myprogram import *

class MathTesting(unittest.TestCase):
    def __init__(self, methodName: str = "runTest", operasi=None) -> None:
        super().__init__(methodName)
        self.add = Operations.add
        self.substract = Operations.substract
        self.multiply = Operations.multiply
        self.divide = Operations.divide
        self.factorialize = Operations.factorialize
        self.operation = {
            '1': 'addition',
            '2': 'substraction',
            '3': 'multiplication',
            '4': 'division',
            '5': 'factorialization'
        }

    def testResult(self):
        # Pemanggilan fungsi dinamis
        if (1 <= int(operasi) <= 5):
            func = getattr(self, self.operation[operasi]) # Mengambil nama fungsi berdasarkan string dari dictionary operation
            func() # Memanggil fungsi

    def addition(self):
        self.assertEqual(self.add(bilangan_1, bilangan_2), sum((bilangan_1, bilangan_2)))
        self.assertTrue(self.add(bilangan_1, bilangan_2) == bilangan_1 + bilangan_2)

    def substraction(self):
        self.assertEqual(self.substract(bilangan_1, bilangan_2), bilangan_1 - bilangan_2)
        self.assertTrue(self.substract(bilangan_1, bilangan_2) == bilangan_1 - bilangan_2)

    def multiplication(self):
        self.assertEqual(self.multiply(bilangan_1, bilangan_2), bilangan_1 * bilangan_2)
        self.assertTrue(self.multiply(bilangan_1, bilangan_2) == bilangan_1 * bilangan_2)

    def division(self):
        self.assertEqual(self.divide(bilangan_1, bilangan_2), bilangan_1 / bilangan_2)
        self.assertTrue(self.divide(bilangan_1, bilangan_2) == bilangan_1 / bilangan_2)

    def factorialization(self):
        self.assertFalse(self.factorialize(bilangan_1) < -1)
        self.assertLess(self.factorialize(bilangan_1), -1)

if __name__ == "__main__":
    unittest.main()