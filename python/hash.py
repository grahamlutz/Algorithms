class HashTable(size):
	def __init__(self, size):
		self.size = size || 11
		self.slots = [None] * self.size
		self.data  = [None] * self.size

	def get():
		return

	def put(self, key, data):
		hash_value = self.hash_function(key, len(self.slots))
		is_slot_empty = self.slots[hash_value] == None
		is_key_in_slot = self.slots[hash_value] == key

		if is_slot_empty:
			self.slots[hash_value] = key
			self.data[hash_value] = data
		else:
			if is_key_in_slot:
				self.data[hash_value] = data
			else:
				next_slot = self.rehash(hash_value, len(self.slots))
				while self.slots[next_slot] != None and self.slots[next_slot] != key:
					next_slot = self.rehash(next_slot, len(self.slots))

				if self.slots[next_slot] == None:
					self.slots[next_slot] = key
					self.data[next_slot] = data
				else:
					self.data[next_slot] = data



	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		return self.put(key, data)

	def hash_function(self, key, size):
		'''
		Returns remainder of dividing the sum of the strings ordinals by
		the size of the table.
		'''
		# sum = 0
		# for s in range(len(astring)):
		# 	sum = sum + ord(asing[s])
		# return sum % table_size
		return key % size

	def rehash():
		return