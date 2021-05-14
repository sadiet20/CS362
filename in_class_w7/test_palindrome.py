'''
Program: In class activity week 7
Author: Sadie Thomas
Date: 5/13/21
Description: test palindrome program using unittest and pytest
'''

import unittest
import palindrome


class testCasePalin(unittest.TestCase):
	def test_palin_true(self):
		self.assertTrue(palindrome.is_palindrome("abccba"))
		self.assertTrue(palindrome.is_palindrome("abcfcba"))
		self.assertTrue(palindrome.is_palindrome("1221"))
		self.assertTrue(palindrome.is_palindrome("hannah"))
		self.assertTrue(palindrome.is_palindrome("1"))
	def test_palin_empty(self):
		self.assertTrue(palindrome.is_palindrome(""))
	def test_palin_false(self):
		self.assertFalse(palindrome.is_palindrome("abc"))
		self.assertFalse(palindrome.is_palindrome("abca"))
		self.assertFalse(palindrome.is_palindrome("12389"))
		self.assertFalse(palindrome.is_palindrome("abccab"))


if __name__ == '__main__':
	unittest.main()




#I ran these tests only when I ran pytests and commented out the unittest parts above
def test_palin_true():
	assert palindrome.is_palindrome("abccba")
	assert palindrome.is_palindrome("abcfcba")
	assert palindrome.is_palindrome("123321")
	assert palindrome.is_palindrome("hannah")
	assert palindrome.is_palindrome("")

def test_palin_false():
	assert not palindrome.is_palindrome("12389")
	assert not palindrome.is_palindrome("abc")
	assert not palindrome.is_palindrome("abccab")
