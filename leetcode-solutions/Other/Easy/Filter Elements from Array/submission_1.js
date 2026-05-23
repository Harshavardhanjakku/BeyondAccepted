# Problem: Filter Elements from Array
# Difficulty: Easy
# Topic: Other
# Language: javascript
# Submission: 1

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const res= arr.filter(fn);
    return res
};
