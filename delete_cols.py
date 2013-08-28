

import csv
import sys
import argparse

parser = argparse.ArgumentParser(description='delete some columns from file, given by their indexes')
parser.add_argument("input_file", help = "path to csv input file")
parser.add_argument("output_file", help = "path to output file")
parser.add_argument('index', metavar='I', type=int, nargs='+',
							help='an index or indexes to delete')
parser.add_argument("-v", "--verbose", help = "will write counts during process to standard out",
					action = "store_true", default = False)

args = parser.parse_args()
args.index.sort( reverse = True )

if args.verbose:
	print "%s ---> %s" % ( args.input_file, args.output_file )
	print "header indices: %s" % ( args.index )

reader = csv.reader(open( args.input_file ))
writer = csv.writer(open( args.output_file, 'wb' ))

counter = 0
for line in reader:
	#deal with empty line
	if not line:
		break

	for h in args.index:
		del line[h]

	writer.writerow( line )

	counter += 1
	if counter % 10000 == 0 and args.verbose:
		print counter
