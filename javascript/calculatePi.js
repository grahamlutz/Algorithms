
function pi(pointsArray) {
	let pointsInsideDisk = 0;

	pointsArray.map( (point) => {
		if ( (point[0] ** 2) + (point[1] ** 2) <= 1 ) pointsInsideDisk++
	})

	let pi = (pointsInsideDisk / pointsArray.length) * 4

	return pi
}

let points = [];
for (let i = 0; i < 10000; i++) {
	let x = Math.random()
	let y = Math.random()
	points.push([x,y])
}

console.log(pi(points));