// Selection sort loops over positions in the array. For each position, it 
// finds the index of the minimum value in the subarray starting at that position. 
// Then it swaps the values at the position and at the minimum index. 

var swap = function(array, firstIndex, secondIndex) {
    var temp = array[firstIndex];
    array[firstIndex] = array[secondIndex];
    array[secondIndex] = temp;
};

var indexOfMinimum = function(array, startIndex) {

    var minValue = array[startIndex];
    var minIndex = startIndex;

    for(var i = minIndex + 1; i < array.length; i++) {
        if(array[i] < minValue) {
            minIndex = i;
            minValue = array[i];
        }
    } 
    return minIndex;
}; 

var selectionSort = function(array) {
    var min;
    for( var i = 0; i <array.length; i++ ) {
        min = indexOfMinimum(array, i);
        swap(array, min, i);
    }
};

var array = [22, 11, 99, 88, 9, 7, 42];
selectionSort(array);
println("Array after sorting:  " + array);
