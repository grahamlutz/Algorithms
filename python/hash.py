def hash(astring, table_size):
	'''
	Returns remainder of dividing the sum of the strings ordinals by
	the size of the table.
	'''
	sum = 0
	for s in range(len(astring)):
		sum = sum + ord(asing[s])
	return sum % table_size