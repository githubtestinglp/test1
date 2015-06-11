import numpy as np 

def f(in1,in2):
	return in1**in2



if __name__ == "__main__":
	in1 = float(raw_input('value 1: '))
	in2 = float(raw_input('exponent: '))
	print("result: %.0f" % f(in1,in2))
	mylist = [1,2,3,4]
	mylist2 = map(lambda x: x**2, mylist)
	print mylist, mylist2
