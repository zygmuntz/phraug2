'''
split a file into two randomly, line by line. 
'''

import argparse
import sys
import random

parser = argparse.ArgumentParser( description = "split a file into two randomly, line by line." )
parser.add_argument( "input_file", help = "path to an input file" )
parser.add_argument( "output_file1", help = "path to the first output file" )
parser.add_argument( "output_file2", help = "path to the second output file" )
parser.add_argument( "-p", "--probability", help = "probability of writing to the first file (default 0.9)",
	default = 0.9, type = float )
parser.add_argument( "-r", "--random_seed", help = "random seed", default = False )
parser.add_argument( "-s", "--skip_headers", help = "skip the header line", 
	default = False, action = 'store_true' )

args = parser.parse_args()

if args.random_seed:
	random.seed( args.random_seed )

i = open( args.input_file )
o1 = open( args.output_file1, 'wb' )
o2 = open( args.output_file2, 'wb' )

if args.skip_headers:
	i.readline()

counter = 0

for line in i:
	r = random.random()
	if r > args.probability:
		o2.write( line )
	else:
		o1.write( line )
	
	counter += 1
	if counter % 100000 == 0:
		print counter
	

		
		
		
		
		
		
		
