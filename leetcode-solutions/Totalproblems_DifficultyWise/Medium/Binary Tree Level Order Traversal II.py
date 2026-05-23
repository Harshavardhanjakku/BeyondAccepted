# Binary Tree Level Order Traversal II
# Difficulty: Medium
# Language: python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        q=deque()
        res=[]
        if root is None:
            return res
        else:
            q.append(root)
            while q:
                    nodelist = []  
                    datalist = []
                    for _ in range(len(q)):
                        node = q.popleft()
                        datalist.append(node.val)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                    res.append(datalist)
            return res[::-1]
        
