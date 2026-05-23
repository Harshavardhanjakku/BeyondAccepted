# Problem: Flipping an Image
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        rl=[x[::-1] for x in image]
        il=[]
        for i in rl:
            nl=[]
            for j in i:
                nl.append(int(not j))
            il.append(nl)
        return il        
