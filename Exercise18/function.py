def print_two(*args):
	print args
	print "arg1: %r, arg2: %r" % (args[0], args[1])

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothing."

print_two("Zed", "shaw", "1","3",1,2,3,4,5,6,7,8,0)
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

