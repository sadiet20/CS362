'''
Program: HW 7
Author: Sadie Thomas
Date: 5/31/21
Description: demonstrate test-first development with FizzBuzz program
'''

import unittest
import fizz


class testCaseFizz(unittest.TestCase):
	def test_normal(self):
		self.assertEqual(fizz.FizzBuzz(2), 2)
	def test_normal2(self):
		self.assertEqual(fizz.FizzBuzz(17), 17)
	def test_threes(self):
		self.assertEqual(fizz.FizzBuzz(3), "Fizz")


if __name__ == '__main__':
	unittest.main()
