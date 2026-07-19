# Problem: Apply Transform Over Each Element in Array
# Difficulty: Easy
# Topic: Other
# Language: javascript
# Submission: 4

var map = function(arr, fn) {  
    const res = [ ]
    for (i=0 ;i<arr.length;i++)
    {
        res.push(fn(arr[i],i));
    }
    return res;
};
