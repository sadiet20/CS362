'''
Sadie Thomas
CS 362 - HW4
5/3/21
Testing framework for average.py
'''

import unittest
import average


class testCaseAverage(unittest.TestCase):
	def test_average(self):
		self.assertEqual(average.average([12, 13, 53, 2]), 20)
		self.assertAlmostEqual(average.average([12.2, 1, 8.2]), 7.13, 2)
	def test_average_zero(self):
		self.assertEqual(average.average([]), 0)
	def test_average_fail(self):
		self.assertEqual(average.average(["hi", "you"]), 0)		#this fails because of strings

if __name__ == '__main__':
	unittest.main()
