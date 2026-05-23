# Problem: Check Completeness of a Binary Tree
# Difficulty: Medium
# Topic: Tree
# Language: python
# Submission: 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        q=deque()
        flag=False
        q.append([root])
        while q:
            nodelist=q.popleft()
            for node in nodelist:
                if node is None :
                    flag=True
                else:
                    q.append([node.left,node.right]) 
                    if flag and node :
                        return False
        return True
        
