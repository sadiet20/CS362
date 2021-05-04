'''
Sadie Thomas
CS 362 - HW4
5/3/21
Testing framework for volume.py
'''

import unittest
import volume


class testCaseVolume(unittest.TestCase):
		
	def test_volume(self):
		self.assertEqual(volume.volume(1, 10, 3), 30)
		self.assertAlmostEqual(volume.volume(100, 2.1, 23.45), 4924.5, 1)
	def test_volume_string(self):
		self.assertRaises(TypeError, volume.volume, "this", "should", "TypeError")
	def test_volume_fail(self):
		self.assertEqual(volume.volume(2, 2, -2), 0)	#this test will fail bc negative


if __name__ == '__main__':
	unittest.main()
