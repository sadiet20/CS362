'''
Program: HW 7
Author: Sadie Thomas
Date: 5/31/21
Description: demonstrates test-first development with leap year program
'''

import unittest
import leap


class testCaseLeap(unittest.TestCase):
	def test_non_leap(self):
		self.assertFalse(leap.is_leap(5))
	def test_div4(self):
		self.assertTrue(leap.is_leap(64))

if __name__ == '__main__':
	unittest.main()