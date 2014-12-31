'''
# using while-loops

i = 0
numbers = []
while i < 200:
	print "At the top i is %d" % i
	numbers.append(i)

	i += 10
	print "Numbers now: ", 
	print numbers
	print "At the bottom i is %d" % i

print "The numbers: " 

for num in numbers:
	print num
'''

# using for-loops
i = 0
numbers = []

for i in range(0, 6):

	numbers.append(i)
	print "At the top i is %d" % numbers[i]
	print "Numbers now:" 
	print numbers
	print "At the bottom i is %d" % (i + 1)

print "the array of numbers now is: " 
print numbers




