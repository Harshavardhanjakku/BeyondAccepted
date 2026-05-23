# Word Search
# Difficulty: Medium
# Language: python

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m=len(board)
        n=len(board[0])
        length=len(word)
        if m*n < length :
            return False
        visited=[[0 for _ in range(n)] for _ in range(m)]
        def dfs(r,c,ind):
            if r<0 or c<0 or  r>=m or c>=n or board[r][c]!=word[ind] or visited[r][c]:
                return False
            if ind==length-1:
                return True 
            visited[r][c]=1
            found = dfs(r,c+1,ind+1) or dfs(r,c-1,ind+1) or dfs(r+1,c,ind+1) or dfs(r-1,c,ind+1) 
            visited[r][c]=0 
            return found
                
        for i in range(m):
            for j in range(n):
                row,col=i,j
                if board[i][j]==word[0]:
                    if dfs(row,col,0):
                        return True
        return False

