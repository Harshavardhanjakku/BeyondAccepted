# Problem: Lemonade Change
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def lemonadeChange(self, bills):
        r5 = 0
        r10 = 0
        for bill in bills:
            if bill == 5:
                r5 += 1
            elif bill == 10:
                if r5 == 0:
                    return False
                r5 -= 1
                r10 += 1
            else:   
                if r10 > 0 and r5 > 0:
                    r10 -= 1
                    r5 -= 1
                elif r5 >= 3:
                    r5 -= 3
                else:
                    return False
        return True

