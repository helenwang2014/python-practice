from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s. " % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "Does output file exist?  %s " % exists(to_file)

print "Ready, hit RETURN to continue, CTRL-C to abort. "
raw_input()

out_file = open('to_file', 'w')
print out_file.write(indata)

in_file.close()
out_file.close()

