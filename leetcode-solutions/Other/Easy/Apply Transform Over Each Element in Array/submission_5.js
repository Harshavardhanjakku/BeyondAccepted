# Problem: Apply Transform Over Each Element in Array
# Difficulty: Easy
# Topic: Other
# Language: javascript
# Submission: 5

var map = function(arr, fn) {  
    return arr.map((val, i) => fn(val, i));
};
