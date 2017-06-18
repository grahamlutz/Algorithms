class HashTable(size):
	def __init__(self, size):
		self.size = size || 11
		self.slots = [None] * self.size
		self.data  = [None] * self.size

	def get():
		return

	def put():
		return

	def __getitem__(self, key):

	def __setitem__(self, ket, data):


	def hash_function(astring, table_size):
		'''
		Returns remainder of dividing the sum of the strings ordinals by
		the size of the table.
		'''
		sum = 0
		for s in range(len(astring)):
			sum = sum + ord(asing[s])
		return sum % table_size

	def rehash():
		return