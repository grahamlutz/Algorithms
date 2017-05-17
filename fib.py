
'''
Write a function fib() that a takes an integer nn and returns the nth fibonacci number. 
The Fibonacci series is a numerical series where each item is the sum of the two previous items. It starts off like this:
0,1,1,2,3,5,8,13,21...
'''

def fib(n):
	if n == 0: 
		return 0
	prev = 0
	curr = 1

	for i in range(0,n-1):
		next_num = curr + prev
		prev = curr
		curr = next_num

	print 'current number: ' + str(curr)


fib(8)