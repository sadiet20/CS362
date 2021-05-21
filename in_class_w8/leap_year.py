'''
Program: In class activty w8
Author: Sadie Thomas
Date: 5/20/21
Description: determines if a year is a leap year
Inputs: a year (number)
Outputs: true or false
Running instructions: My program runs on python3, so if you are using the terminal you can run the command $python3 sadie_thomas_hw1.py
'''



'''
Function: check_leap
Description: prints out if a number is a leap year or not
Parameters: year to be tested
Pre-conditions: year is a positive integer
Post-conditions: printed if year is a leap year or not
'''
def is_leap(year: int):
	if(year%4==0):
		if(year%400==0):
			return True
		elif(year%100==0):
			return False
		else:
			return True
	else:
		return False


#function calls for checking coverage
is_leap(100)
is_leap(4)
is_leap(123)
is_leap(800)
is_leap(111)
