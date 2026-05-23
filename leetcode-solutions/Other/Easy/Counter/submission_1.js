# Problem: Counter
# Difficulty: Easy
# Topic: Other
# Language: javascript
# Submission: 1

var createCounter = function(n) {
    return function() {
        return n++;
    };
};
