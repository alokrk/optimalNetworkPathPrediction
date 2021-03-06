#Script by John Costella to create the predictions using Markov Chain
'take paths optimality file, output a prediction file using markov chains'

import sys, csv
from transition_utils import *


def get_predictions( data ):

	if sum( data ) == 0:
		return [ 0 for x in range( 0, 3 ) ]

	transitions = get_transitions( data )
	transition_probs = get_transition_probs( transitions )
	predictions = forecast_five( data[-1], transition_probs )
	return predictions


###

input_file = sys.argv[1]
output_file = sys.argv[2]

i = open( input_file )
o = open( output_file, 'wb' )

reader = csv.reader( i )

periods = [ [] for x in range( 0, 3 )]

for line in reader:
	#print len(line)
	line = line[:12]
	#print len(line)
	line = map( int, line)
        #print line
	predictions = get_predictions( line )

	for i, period in enumerate( periods ):
		period.append( predictions[i] )
        #break
predicted = reduce( lambda x, y: x + y, periods )

#assert( len( predicted ) == 50000 )
for p in predicted:
	o.write( "%s\n" % ( p ))
