# Problem: Maximum Ice Cream Bars
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 3

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = max(costs)
        barcost = [0] * (n + 1)
        for cost in costs:
            barcost[cost] += 1
        totalbars = 0
        for cost in range(1, n + 1):
            nofbars = barcost[cost]
            if nofbars == 0:
                continue
            bars = min(nofbars, coins // cost)
            totalbars += bars
            coins -= bars * cost
            if coins < cost:
                break
        return totalbars
