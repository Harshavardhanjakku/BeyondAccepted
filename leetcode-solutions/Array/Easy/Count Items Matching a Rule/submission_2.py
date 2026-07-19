# Problem: Count Items Matching a Rule
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        total=0
        for item in items :
            if (ruleKey=="type" and ruleValue== item[0]) or (ruleKey=="color" and ruleValue== item[1] ) or (ruleKey=="name" and ruleValue== item[2]  ):
                total+=1
        return total

