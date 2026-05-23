# Problem: Construct the Rectangle
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 4

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        i=int(area**0.5)
        if i*i==area:
            return [i,i]
        else:
            for j in range(i,area+1):
                if area%j==0:
                    break
                else:
                    j+=1
            if area//j<j:
                        return [j,area//j]
            else:
                        return [area//j,j]
