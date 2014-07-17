#!/usr/bin/env python

"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[3]) if there are no labels in your file.
Expecting no headers. If present, headers can be skipped with argv[4] == 1.
"""

import sys
import csv
import argparse

def construct_line( label, line ):
	new_line = []
	if float( label ) == 0.0:
		label = "0"
	new_line.append( label )
	
	for i, item in enumerate( line ):
		if item == '' or float( item ) == 0.0:
			continue
		new_item = "%s:%s" % ( i + 1, item )
		new_line.append( new_item )
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line

# ---

parser = argparse.ArgumentParser()
parser.add_argument( "input_file", help = "path to the CSV input file" )
parser.add_argument( "output_file", help = "path to the output file" )

parser.add_argument( "-l", "--label-index", help = "zero based index for the label column. If there are no labels in the file, use -1.",
					 type = int, default = 0 )

parser.add_argument( "-s", "--skip-headers", help = "Use this switch if there are headers in the input file.", action = 'store_true' )

args = parser.parse_args()

#	

i = open( args.input_file )
o = open( args.output_file, 'wb' )

reader = csv.reader( i )
if args.skip_headers:
	headers = reader.next()

for line in reader:
	if args.label_index == -1:
		label = 1
	else:
		label = line.pop( args.label_index )
		
	new_line = construct_line( label, line )
	o.write( new_line )
	