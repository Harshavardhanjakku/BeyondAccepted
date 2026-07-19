# Problem: Maximum Ice Cream Bars
# Difficulty: Medium
# Topic: Array
# Language: python3
# Submission: 1

class Solution:
    def maxIceCream(self, costs, coins):
        totalbars=0
        costs.sort()
        for cost in costs:
            if cost > coins :
                break
            coins-=cost
            totalbars+=1
        return totalbars
        
            
       
