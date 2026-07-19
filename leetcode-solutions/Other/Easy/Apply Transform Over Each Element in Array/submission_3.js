# Problem: Apply Transform Over Each Element in Array
# Difficulty: Easy
# Topic: Other
# Language: javascript
# Submission: 3

var map = function(arr, fn) {  
    const res = [ ]
    return arr.map((value,i)=>fn(value,i));
};
