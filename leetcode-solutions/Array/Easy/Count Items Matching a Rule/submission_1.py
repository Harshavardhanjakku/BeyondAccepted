# Problem: Count Items Matching a Rule
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        mp = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        count = 0
        idx = mp[ruleKey]
        for item in items:
            if item[idx] == ruleValue:
                count += 1
        return count
