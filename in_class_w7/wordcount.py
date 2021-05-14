'''
Program: In class activity week 7
Author: Sadie Thomas
Date: 5/13/21
Description: counts the number of words in a phrase
'''


'''
Function: count_words
Description: counts the number of words in a phrase
Parameters: string to be counted
Pre-conditions: none
Post-conditions: returns number of words in phrase
'''
def count_words(phrase):
	count = 0;
	for i in range(1, len(phrase)):
		if(phrase[i]==' ' and phrase[i-1]!=' '):
			count = count+1
	if(len(phrase)>0 and phrase[len(phrase)-1]!=' '):
		count = count+1
	return count


#I commented out the code below when I ran pytest
def main():
	phrase = input("Enter a phrase: ")
	count = count_words(phrase)
	print("There are", count, "words in the phrase '" + phrase + "'")

main()
