'''
Program: HW 7
Author: Sadie Thomas
Date: 5/31/21
Description: demonstrates test-first development with leap year program
'''


def is_leap(year):
	if(year % 100 == 0):
		return False
	if(year % 4 == 0):
		return True
	return False
