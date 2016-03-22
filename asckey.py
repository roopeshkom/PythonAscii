print "Please enter the sizes of the array:"
dim1, dim2 = raw_input('> ').split()
x = [["@" for _ in range(int(dim2))] for _ in range(int(dim1))]
for i in range(len(x)):
	str = ""
	print "   ",
	for j in range(len(x[0])):
		str += "%s -> " % x[i][j]
	print str.rstrip(' -> ')
	if(i != (len(x)-1)):		
		print "    |" * len(x[0])
		print "    v" * len(x[0])