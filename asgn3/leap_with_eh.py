'''
Program: HW 3
Author: Sadie Thomas
Date: 4/25/21
Description: determines if a year is a leap year (with error handling)
Inputs: a year (number)
Outputs: yes or no
Running instructions: My program runs on python3, so if you are using the terminal you can run the command $python3 leap_with_eh.py
'''

def main():
	while(1):
		user_input = input("Enter a year: ")

		#error handling for non-digits and negative numbers
		if(not user_input.isdigit()):
			print("[ERROR] You must enter a positive integer")
			continue

		year = int(user_input)
		check_leap(year)

		#option to check more numbers
		repeat = input("\nWould you like to test another number? Enter 1 for yes or anything else to quit: ")
		if(repeat!="1"):
			break
		
	print("Thanks!")


'''
Function: check_leap
Description: prints out if a number is a leap year or not
Parameters: year to be tested
Pre-conditions: year is a positive integer
Post-conditions: printed if year is a leap year or not
'''
def check_leap(year: int):
	if(year%4==0):
		if(year%400==0):
			print(year, "is a leap year")
		elif(year%100==0):
			print(year, "is not a leap year")
		else:
			print(year, "is a leap year")
	else:
		print(year, "is not a leap year")


main()
