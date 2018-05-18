import unittest
from calculations import Calculations

class TestCalculation(unittest.TestCase):
    def testAdditionNumbers(self):
        self.assertEqual(Calculations.addition(2,3),5)
    def testAdditionNegatives(self):
        self.assertEqual(Calculations.addition(-2,3),1)
    def testAdditionFalseOutput(self):
        self.assertNotEqual(Calculations.addition(2,3),8)    
    def testAdditionString(self):
        with self.assertRaises(TypeError):
            Calculations.addition("two",3)

if __name__ == '__main__':
    unittest.main()

