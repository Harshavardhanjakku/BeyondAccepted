# Problem: Find Largest Value in Each Tree Row
# Difficulty: Medium
# Topic: Tree
# Language: python3
# Submission: 4

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=deque()
        q.append([root])
        res=[]
        while q :
            nodes=q.popleft()
            maxi=float('-inf')
            temp=[]
            for node in nodes:
                maxi=max(node.val,maxi)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                q.append(temp)
            res.append(maxi)
        return res
