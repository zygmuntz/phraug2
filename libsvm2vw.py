import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help = "path to csv input file")
parser.add_argument("output_file", help = "path to output file")

args = parser.parse_args()

i = open( args.input_file )
o = open( args.output_file, 'wb' )

for line in i:
	y, x = line.split( " ", 1 )
	new_line = y + " |n " + x
	o.write( new_line )
