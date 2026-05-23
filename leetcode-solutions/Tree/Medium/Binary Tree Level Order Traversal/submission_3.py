# Problem: Binary Tree Level Order Traversal
# Difficulty: Medium
# Topic: Tree
# Language: python
# Submission: 3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        q=deque()
        res=[]
        if root is None:
            return res
        else:
            q.append(root)
            while q:
                    datalist = []
                    n=len(q)
                    for _ in range(n):
                        node = q.popleft()
                        datalist.append(node.val)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                    res.append(datalist)
            return res
        
