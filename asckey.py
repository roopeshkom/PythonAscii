#Imports a random number picker and a colored text printer
from termcolor import colored
from random import randint

#This loops repeats until we get the input we need to progress
while(True):
	try:
		#Takes the user input for the size of the 2D array
		print "Please enter the dimensions of the matrix, in the format nxm (ex: 1x2)"
		dim1, dim2 = raw_input('> ').split('x', 1)
		dim1 = int(dim1)
		dim2 = int(dim2)

		#Prevents the user from inputing values that are too large or negative
		if(not(0<dim1<15 and 0<dim2<15)):
			print "Please enter valid (between 1 and 15, exclusive) values!"
			continue

		#This initializes the nxm array specified by the user with 'o' characters
		x = [['o' for _ in range(dim2)] for _ in range(dim1)]
	except Exception as e:
		#Redo the loop in the case of bad input
		print e.args 
		print "The values aren't in the proper format!"
		continue
	else:
		#This code turns some of the array items into a red X and breaks loop
		x[randint(0, (len(x)-1))][randint(0, (len(x[0])-1))] = colored("X", "red")
		break

#Iterates through the 2d array
for i in range(len(x)):
	str = ""
	print " " * 3,

	#Adds the -> to the printed array
	for j in range(len(x[0])):
		str += "%s -> " % x[i][j]

	#Removes unnecessary -> and adds vertical arrows as well
	print str.rstrip(' -> ')
	if(i != (len(x)-1)):		
		print "    |" * len(x[0])
		print "    v" * len(x[0])

#Finishing messages lets user know the program is finished
print "I hope you enjoy your matrix... now",
print colored("run me again!", "blue"),
print colored(":)", "magenta")