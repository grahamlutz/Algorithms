/*
Write a function fib() that a takes an integer nn and returns the nth fibonacci number. 
The Fibonacci series is a numerical series where each item is the sum of the two previous items. It starts off like this:
0,1,1,2,3,5,8,13,21...
*/

let fibNum = process.argv[2];

function fib(n) {
	if (n == 0) return 0;

	let prev = 0;
	let curr = 1;

	while (n--) {
		[ prev, curr ] = [ curr, prev + curr ]
	}

	return curr
}

console.log(fib(fibNum))