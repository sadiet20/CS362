#Sadie Thomas
#Testing framework for calc.py

import unittest
import calc


class testCaseCalc(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.add(10, 5), 15)
		self.assertEqual(calc.add(2, 2), 4)
		self.assertEqual(calc.add(-3, 0), -3)
	def test_add_fail(self):
		self.assertEqual(calc.add(2, 2), 5)
	def test_subtract(self):
		self.assertEqual(calc.subtract(6, 7), -1)
		self.assertEqual(calc.subtract(100, 0), 100)
	def test_subtract_fail(self):
		self.assertEqual(calc.subtract(4, 15), 3)
	def test_multiply(self):
		self.assertEqual(calc.multiply(4, 5), 20)
		self.assertEqual(calc.multiply(2, 0), 0)
		self.assertEqual(calc.multiply(-2, 4), -8)
	def test_multiply_fail(self):
		self.assertEqual(calc.multiply(-2, -2), -4)
	def test_divide(self):
		self.assertEqual(calc.divide(20, 10), 2)
		self.assertAlmostEqual(calc.divide(10, 3), 3.33, 2)
		self.assertEqual(calc.divide(3, 0), 0)
	def test_divide_fail(self):
		self.assertEqual(calc.divide(50, 10), 500)


if __name__ == '__main__':
	unittest.main()
