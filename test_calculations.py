import unittest
from calculations import Calculations

class TestCalculation(unittest.TestCase):
    def testAdditionNumbers(self):
        result=Calculations.addition(2,3)
        self.assertEqual(result,5)
    def testAdditionNegatives(self):
        result=Calculations.addition(-2,3)
        self.assertEqual(result,1)
    def testAdditionFalseOutput(self):
        result=Calculations.addition(2,3)
        self.assertNotEqual(result,8)    
    def testAdditionString(self):
        with self.assertRaises(TypeError):
            Calculations.addition("two",3)

if __name__ == '__main__':
    unittest.main()

