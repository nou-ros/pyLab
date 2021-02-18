import unittest
import calc

# first we have to create a class
class TestCalc(unittest.TestCase):

    # method must start with test
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1),-2)

    def test_subtract(self):
        result = calc.subtract(10,5)
        self.assertEqual(result, 5)
        self.assertEqual(calc.subtract(-1,1),-2)
        self.assertEqual(calc.subtract(-1,-1),0)
    
    def test_multiply(self):
        result = calc.multiply(10,5)
        self.assertEqual(result, 50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-1,-1),1)
    
    def test_divide(self):
        result = calc.divide(10,5)
        self.assertEqual(result, 2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)
        self.assertEqual(calc.divide(5,2),2.5)
    
    def test_power(self):
        self.assertEqual(calc.power(2,5),32)
        self.assertEqual(calc.power(-1,1),-1)
        self.assertEqual(calc.power(-1,-1),-1)

        with self.assertRaises(ValueError):
            calc.divide(10,0)


# default command without setting main
'''python -m unittest test_calc.py'''

if __name__ == '__main__':
    unittest.main()