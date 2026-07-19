# Problem: Maximum Ice Cream Bars
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 9

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if coins < cost:
                break
            coins -= cost
            count += 1 
        return count
