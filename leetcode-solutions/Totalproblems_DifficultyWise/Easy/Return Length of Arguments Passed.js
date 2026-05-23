# Return Length of Arguments Passed
# Difficulty: Easy
# Language: javascript

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
