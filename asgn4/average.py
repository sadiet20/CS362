'''
Sadie Thomas
CS 362 - HW 4
5/3/21
Calculates average of a list
'''

def average(my_list):
	if(len(my_list)==0):
		return 0
	total_sum = 0
	for i in range(len(my_list)):
		total_sum += my_list[i]
	return total_sum/len(my_list)
