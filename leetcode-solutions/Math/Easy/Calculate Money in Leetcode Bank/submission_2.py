# Problem: Calculate Money in Leetcode Bank
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 2

class Solution(object):
    def totalMoney(self, n):
        day = 1
        total = 0
        start = 1
        week = 1
        while day <= n:
            if day != 1 and (day - 1) % 7 == 0:
                week += 1
                start = week
            total += start
            start += 1
            day += 1
        return total
