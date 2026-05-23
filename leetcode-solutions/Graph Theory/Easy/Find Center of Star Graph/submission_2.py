# Problem: Find Center of Star Graph
# Difficulty: Easy
# Topic: Graph Theory
# Language: python
# Submission: 2

class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        a,b=edges[0],edges[1]
        if a[0]==b[0] or a[0]==b[1]:
            return a[0]
        else:
            return a[1]
