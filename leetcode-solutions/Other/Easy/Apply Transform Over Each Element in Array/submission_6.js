# Problem: Apply Transform Over Each Element in Array
# Difficulty: Easy
# Topic: Other
# Language: javascript
# Submission: 6

var map = function(arr, fn) { 
    const result = arr.map((val, i) => fn(val, i)); 
    return result;
};
