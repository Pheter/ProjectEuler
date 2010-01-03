def getNextNum(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n + 1

def getSequenceLength(n):
    terms = 1
    if n in solved_sequences:
        terms += solved_sequences[n]
    elif n > 1:
        terms += getSequenceLength(getNextNum(n))
        #add terms for n to solved_sequences
        solved_sequences[n] = terms
    return terms

longest_sequence = 0
longest_sequence_term = None
solved_sequences = {}

for i in range (13, 1000000 + 1):
    sequence_length = getSequenceLength(i)
    if sequence_length > longest_sequence:
        longest_sequence = sequence_length
        longest_sequence_term = i

print longest_sequence_term, 'produces', longest_sequence, 'terms.'
