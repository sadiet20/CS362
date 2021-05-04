'''
Sadie Thomas
CS 362 - HW4
5/3/21
Testing framework for name.py
'''

import unittest
import name


class testCaseAverage(unittest.TestCase):
	def test_name(self):
		self.assertEqual(name.combine("Chuck", "Norris"), "Chuck Norris")
	def test_name_num(self):
		self.assertEqual(name.combine(123, 321), "123 321")
	def test_name_fail(self):
		self.assertEqual(name.combine("John", "Doe"), "Dave Davis")		#this will fail


if __name__ == '__main__':
	unittest.main()
