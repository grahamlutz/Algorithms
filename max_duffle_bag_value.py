'''
You are a renowned thief who has recently switched from stealing precious metals to stealing cakes because of the insane profit margins. 
You end up hitting the jackpot, breaking into the world's largest privately owned stock of cakes, the vault of the Queen of England.
While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.

Each type of cake has a weight and a value, stored in a tuple with two indices:

An integer representing the weight of the cake in kilograms
An integer representing the monetary value of the cake in British pounds

You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.

Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.
'''
from operator import itemgetter

def max_duffel_bag_value(cake_tuples, capacity):
	# remove cakes with weight of 0
	cake_tuples = [i for i in cake_tuples if i[0] > 0]
	# sort cakes by value/kg
	cake_values_per_kg = sorted(cake_tuples, key=lambda cake: cake[1]/cake[0], reverse=True)

	duffel_weight = 0
	duffel_value = 0
	remaining_capacity = capacity

	while remaining_capacity:
		for weight, value in cake_values_per_kg:
			if remaining_capacity >= weight:
				duffel_value += value
				remaining_capacity -= weight
				break

	print duffel_value


cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

max_duffel_bag_value(cake_tuples, capacity)
