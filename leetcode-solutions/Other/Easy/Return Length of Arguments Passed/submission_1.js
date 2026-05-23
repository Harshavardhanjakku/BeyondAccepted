# Problem: Return Length of Arguments Passed
# Difficulty: Easy
# Topic: Other
# Language: javascript
# Submission: 1

/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length
    
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
