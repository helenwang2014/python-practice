'''
from sys import argv
script, filename = argv
py = open(filename)

print "Here is your file %s: " % filename
print py.read()

'''
print "Type the file name again: "
file_name = raw_input()

py_name = open(file_name)
print py_name.read()


