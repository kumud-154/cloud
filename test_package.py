import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(1,1),2)
        self.assertEqual(calc.add(50,10),60)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(1,1),0)
        self.assertEqual(calc.subtract(50,10),40)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(1,1),1)
        self.assertEqual(calc.divide(50,10),5)

if  __name__ == '__main__':
    unittest.main() 
