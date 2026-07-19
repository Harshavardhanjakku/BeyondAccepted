# Problem: Maximum Ice Cream Bars
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 10

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for cost in costs:
            if cost<=coins:
                count+=1
                coins-=cost
            else:
                return count
        return count
