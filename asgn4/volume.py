'''
Sadie Thomas
CS 362 - HW 4
5/3/21
Calculates volume of a cube
'''

def volume(x, y, z):
	if(type(x)==str or type(y)==str or type(z)==str):
		raise TypeError("Cannot find volume of strings")
	return x*y*z
