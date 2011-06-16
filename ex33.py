i = 0
numbers = [ ]

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i
	
print "The numbers: "

for num in numbers:
	print num
	
def number_range(max, step):
	i = 0
	this_list = [ ]
	while i < max:
		print "Item: %d" % i
		this_list.append(i)
		i = i + step
	print this_list 

def number_range_using_for(max, step):
	elements = range(0, max, step)
	for item in elements:
		print "Item: %d" % item
	print elements

number_range(10, 2)
number_range_using_for(20, 2)