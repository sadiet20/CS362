'''
Program: HW 7
Author: Sadie Thomas
Date: 5/31/21
Description: demonstrate test-first development with FizzBuzz program
'''

import unittest
#fails because fizz is not created yet
import fizz


class testCaseFizz(unittest.TestCase):
	def test_normal(self):
		self.assertEqual(fizz.FizzBuzz(2), "two")


if __name__ == '__main__':
	unittest.main()
