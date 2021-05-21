#Sadie Thomas
#Testing framework for leap_year.py

import unittest
import leap_year


class testCaseLeap(unittest.TestCase):
	def test_true(self):
		self.assertTrue(leap_year.is_leap(400))
		self.assertTrue(leap_year.is_leap(4))
		self.assertTrue(leap_year.is_leap(2572))
	def test_false(self):
		self.assertFalse(leap_year.is_leap(100))
		self.assertFalse(leap_year.is_leap(2))
		self.assertFalse(leap_year.is_leap(111))
		self.assertFalse(leap_year.is_leap(123))



if __name__ == '__main__':
	unittest.main()
