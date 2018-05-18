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
        result=Calculations.addition('two',3)
        self.assertRaises(self,result,ValueError)

if __name__ == '__main__':
    unittest.main()

