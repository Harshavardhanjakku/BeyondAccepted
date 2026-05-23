# Problem: Number of Provinces
# Difficulty: Medium
# Topic: Depth-First Search
# Language: python
# Submission: 1

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                self.dfs(i, visited, isConnected, n)
        return count

    def dfs(self, i, visited, isConnected, n):
        visited[i] = True
        for j in range(n):
            if isConnected[i][j] == 1 and not visited[j]:
                self.dfs(j, visited, isConnected, n)

