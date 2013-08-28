
import sys
import argparse

parser = argparse.ArgumentParser(description='Count lines in a file')
parser.add_argument("input_file", help = "path to csv input file")
parser.add_argument("-v", "--verbose", help = "will write counts during process to standard out",
					action = "store_true", default = False)
args = parser.parse_args()

f = open( args.input_file )

count =  0
for line in f:
	count += 1

	if count % 100000 == 0 and args.verbose:
		print count

print count
