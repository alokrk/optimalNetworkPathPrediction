from collections import defaultdict

'compute transition probabilities from data'
def get_transitions( data ):

	transitions = { 0: { 0: 0, 1: 0 }, 1: { 0: 0, 1: 0 }}
	
	for i in range( 0, len( data ) - 1 ):
		state = data[i]
		transition = data[i + 1]

		transitions[state][transition] += 1
		
	return transitions
		
		
		
		
'with smoothing'
def get_transition_probs( transitions ):
	
	totals = {}
	totals[0] = sum( transitions[0].values()) + 2
	totals[1] = sum( transitions[1].values()) + 2
	
	probs = {}
	
	for s in [ 0, 1 ]:
		for t in transitions[s]:
			t_count = transitions[s][t]
			t_count += 1

			st = ( s, t )
			
			'''
			print st
			print t_count
			print totals[s]
			'''
			
			probs[st] = 1.0 * t_count / totals[s]
		
	return probs



	
'return probs for each of next state values'
def next_state_probs( s, transition_probs ):
	
		s_to_zero = ( s, 0 )
		s_to_one = ( s, 1 )
		
		return ( transition_probs[s_to_zero], transition_probs[s_to_one] )
		
		
'return probs for each of next state values'
def next_state_probs_uncertain( s, s_prob, transition_probs ):
	
		s2 = int( not s )
		
		to_zero = transition_probs[( s, 0 )] * s_prob   +   transition_probs[( s2, 0 )] * ( 1 - s_prob )
		to_one = transition_probs[( s, 1 )] * s_prob   +   transition_probs[( s2, 1 )] * ( 1 - s_prob )
		
		return ( to_zero, to_one )		
		
		
'return probs for 1 in next 5 periods, starting with a given state'
def forecast_five( s, transition_probs ):
	
		periods = []
		next_one = next_state_probs( s, transition_probs )[1]
		
		periods.append( next_one )
		
		for i in range( 1, 5 ):
			one_prob = periods[i - 1]
			next_one = next_state_probs_uncertain( 1, one_prob, transition_probs )[1]
			periods.append( next_one )
	
		return periods		
