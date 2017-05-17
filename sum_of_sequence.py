#
# sum up any sequence of consecutive integers
#

def sum_of_sequence(list):
	listLength = len(list)
	first = list[0]
	last = list[listLength-1]

	sum = (first + last) * (float(listLength) / 2)
	print sum

sequence = [0,1,2,3,4,5,6]
sum_of_sequence(sequence)
