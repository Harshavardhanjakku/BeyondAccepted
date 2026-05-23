# Find Missing and Repeated Values
# Difficulty: Easy
# Language: python3

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        actualsum=0
        actualsquaresum=0
        n=len(grid)
        n=n*n
        for i in grid:
            for j in i:
                actualsum+=j
                actualsquaresum+=j*j
        sumofnatural=((n)*(n+1))//2
        sumofsquares=((n)*(n+1)*(2*(n)+1))//6
        diff=sumofnatural-actualsum
        addition=(sumofsquares-actualsquaresum)//diff
        return (addition-diff)//2, (addition+diff)//2
        

