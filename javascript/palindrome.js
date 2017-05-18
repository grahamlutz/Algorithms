
var firstCharacter = function(str) {
    return str.slice(0, 1);
};

var lastCharacter = function(str) {
    return str.slice(-1);
};

var middleCharacters = function(str) {
    return str.slice(1, -1);
};

var isPalindrome = function(str) {
    // base case #1
    if (str.length <= 1) {
        return true;   
    }
    // base case #2
    if (firstCharacter(str) !== lastCharacter(str)){
        return false;
    }
    // recursive case
    return isPalindrome(middleCharacters(str));
};

var checkPalindrome = function(str) {
    console.log("Is this word a palindrome? " + str);
    console.log(isPalindrome(str));
};

checkPalindrome("a");
checkPalindrome("motor");
checkPalindrome("rotor");