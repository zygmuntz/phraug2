'''
split a file into a given number of chunks randomly, line by line.
Usage: chunk.py <input file> <number of chunks> [<seed>]'
'''

import sys
import random
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument( "input_file", help = "path to the input file")
parser.add_argument( "num_chunks", help = "number of chunks to split the input file into", type = int )
parser.add_argument( "-s", "--seed", help = "sets a seed for the random number generator", default = None )

args = parser.parse_args()

if args.seed:
	print "seeding: %s" % ( args.seed )
	random.seed( args.seed )

basename = os.path.basename( args.input_file )
basename, ext = os.path.splitext( basename )

i = open( args.input_file )

os = {}
for n in range( args.num_chunks ):
	output_file = "%s_%s%s" % ( basename, n, ext )
	os[n] = open( output_file, 'wb' )

counter = 0

for line in i:
	n = random.randint( 0, args.num_chunks - 1 )
	os[n].write( line )

	counter += 1
	if counter % 100000 == 0:
		print counter


