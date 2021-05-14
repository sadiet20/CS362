'''
Program: In class activity week 7
Author: Sadie Thomas
Date: 5/13/21
Description: test wordcount program using unittest and pytest
'''

import unittest
import wordcount


class testCaseWord(unittest.TestCase):
	def test_word_normal(self):
		self.assertEqual(wordcount.count_words("this is a test"), 4)
		self.assertEqual(wordcount.count_words("hello"), 1)
		self.assertEqual(wordcount.count_words("How many words is this?"), 5)
		self.assertEqual(wordcount.count_words("two words"), 2)
	def test_word_unique(self):
		self.assertEqual(wordcount.count_words(""), 0)
		self.assertEqual(wordcount.count_words(" "), 0)
		self.assertEqual(wordcount.count_words(" hi "), 1)
		self.assertEqual(wordcount.count_words("weird      spacing     "), 2)


if __name__ == '__main__':
	unittest.main()




#I ran only these functions with pytest and commented out the unittest functions above
def test_word_normal():
	assert wordcount.count_words("this is a test") == 4
	assert wordcount.count_words("hello") == 1
	assert wordcount.count_words("How many words is this?") == 5
	assert wordcount.count_words("two words") == 2

def test_word_unique():
	assert wordcount.count_words("") == 0
	assert wordcount.count_words(" ") == 0
	assert wordcount.count_words(" hi ") == 1
	assert wordcount.count_words("weird      spacing      ") == 2
