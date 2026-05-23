# Problem: Construct the Rectangle
# Difficulty: Easy
# Topic: Math
# Language: python
# Submission: 5

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
            while (i<=area):
                if area%i==0:
                    break
                else:
                    i+=1
            if area//i<i:
                        return [i,area//i]
            else:
                        return [area//i,i]
