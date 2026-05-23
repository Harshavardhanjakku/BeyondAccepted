# Counter
# Difficulty: Easy
# Language: javascript

var createCounter = function(n) {
    return function() {
        return n++;
    };
};
