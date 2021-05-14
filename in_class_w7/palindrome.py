'''
Program: In class activity week 7
Author: Sadie Thomas
Date: 5/13/21
Description: determines if a string is a palindrome
'''


'''
Function: is_palindrome
Description: returns true or false if a string is a palindrome
Parameters: string to be tested
Pre-conditions: none
Post-conditions: returns true or false if string is a palindrome
'''
def is_palindrome(string):
	for i in range(len(string)//2):
		if(string[i] != string[len(string)-1-i]):
			return False
	return True


#I commented out the code below when running pytest
def main():
	string = input("Enter a string: ")
	if(is_palindrome(string)):
		print(string, "is a palindrome")
	else:
		print(string, "is not a palindrome")


main()
