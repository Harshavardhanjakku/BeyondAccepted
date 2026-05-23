# Problem: Binary Tree Maximum Path Sum
# Difficulty: Hard
# Topic: Dynamic Programming
# Language: python
# Submission: 2

class Solution(object):
    def maxPathSum(self,root):
        self.MAXI=float('-inf')
        def dfs(node):
            if not node:
                return 0
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))
            self.MAXI=max(self.MAXI,node.val+left+right)
            return node.val+max(left,right)
        dfs(root)
        return self.MAXI
