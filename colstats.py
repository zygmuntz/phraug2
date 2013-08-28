"""
compute column means and standard deviations from data in csv file
"""

import sys, csv
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help = "path to csv input file")
parser.add_argument("output_file", help = "path to output file")

parser.add_argument("--header", help = "Specify if file has header",
					 action="store_true", default = False)

parser.add_argument("-label_index", "--label_index", help = "Specify label index",
					 type = int, default = False)

args = parser.parse_args()


i = open( args.input_file )
reader = csv.reader( i )
writer = csv.writer( open( args.output_file, 'wb' ))

# check headers

if args.header:
	first_line = reader.next()

n = 0

for line in reader:
	n += 1

	#to handle empty lines at the end if file
	if not line:
		break

	if args.label_index:
		line.pop( args.label_index )

	x = np.array( map( float, line ))
	x2 = np.square( x )

	# First pass initialize np arrays
	if n == 1:
		sums_x = x
		sums_x2 = x2
	else:
		sums_x += x
		sums_x2 += x2


# preparation

print n
print sums_x
print sums_x2

means = sums_x / n
sums2_x = np.square( sums_x )

#print means
#print sums2_x

variances = sums_x2 / n - sums2_x / ( n ** 2 )
standard_deviations = np.sqrt( variances )

#print variances
#print standard_deviations

# save stats
if args.header:
   writer.writerow( first_line )

writer.writerow( means )
writer.writerow( standard_deviations )
