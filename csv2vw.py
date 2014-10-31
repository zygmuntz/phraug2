'Convert CSV file to Vowpal Wabbit format.'
'Will work with numerical data only (no categorical columns)'

import sys
import csv
import argparse

def construct_line( label, line ):
	new_line = []
	try:
		label = float( label )
	except Exception, e:
		pass

	if label == 0.0:
		if args.convert_zeros:
			label = "-1"
		else:
			label = "0"
			
	new_line.append( "%s |n " % ( label ))

	for i, item in enumerate( line ):
		try:
			item = float( item )
		except ValueError, e:
			pass
		if item == 0.0:
			continue    # sparse!!!
		new_item = "%s:%s" % ( i + 1, item )
		new_line.append( new_item )
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line

# ---

parser = argparse.ArgumentParser( description = 'Convert CSV file to Vowpal Wabbit format.' )
parser.add_argument( "input_file", help = "path to csv input file" )
parser.add_argument( "output_file", help = "path to output file" )

parser.add_argument( "-l", "--label_index", help = "index of label column (default 0, use -1 if there are no labels)", type = int, default = 0 )

parser.add_argument( "-i", "--ignore_columns", help = "index(es) of columns to ignore, for example 3 or 3,4,5 (no spaces in between)" )

parser.add_argument( "-s", "--skip_headers", help = "use this option if there are headers in the file - default false", action = "store_true" )

parser.add_argument( "-z", "--convert_zeros", help = "convert labels for binary classification from 0 to -1", action = 'store_true', default = False )

args = parser.parse_args()

###

ignore_columns = []
	
if args.ignore_columns:
	ignore_columns = args.ignore_columns.split( ',' )
	ignore_columns = map( int, ignore_columns )
	print "ignoring columns", ignore_columns
	
if args.label_index >= 0:
	ignore_columns.append( args.label_index )	
	
ignore_columns.sort( reverse = True )	# for later popping

###

i = open( args.input_file )
o = open( args.output_file, 'w' )

reader = csv.reader( i )
if args.skip_headers:
	headers = reader.next()

n = 0

for line in reader:
	if args.label_index < 0:
		label = 1
	else:
		label = line[args.label_index]
		
	# drop ignored columns and/or label	
	if ignore_columns:	
		for ic in ignore_columns:
			line.pop( ic )

	new_line = construct_line( label, line )
	o.write( new_line )

	n += 1
	if n % 10000 == 0:
		print n


