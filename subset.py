'Save a subset of lines from an input file; start at offset and count n lines'
'default 100 lines starting from 0'

import sys
import argparse

parser = argparse.ArgumentParser( description = "Save a subset of lines from the input file to the output file" )
parser.add_argument( "input_file", help = "path to input file" )
parser.add_argument( "output_file", help = "path to output file" )
parser.add_argument( "-o", "--offset", help = "line number to start from, default 0", type = int, default = 0 )
parser.add_argument( "-l", "--lines", help = "number of lines to write, default 100", type = int, default = 100 )

args = parser.parse_args()


	
try:
	lines = int( sys.argv[4] )
except IndexError:
	lines = 100	


i = open( args.input_file )
o = open( args.output_file, 'wb' )

offset = args.offset
count = 0

for line in i:

	if offset > 0:
		offset -= 1
		continue

	o.write( line )
	count += 1
	
	if count >= args.lines:
		break
	

		
		
		
		
		
		
		