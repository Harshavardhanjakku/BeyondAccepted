# Problem: Apply Transform Over Each Element in Array
# Difficulty: Easy
# Topic: Other
# Language: javascript
# Submission: 2

var map = function(arr, fn) {  
    const res = [ ];
    const n=arr.length;
    for (i=0 ;i<n;i++)
    {
        res.push(fn(arr[i],i));
    }
    return res;
};
