# Problem: Validate Binary Search Tree
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
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        res=[]
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        n=len(res)
        if n<=1:
            return True
        for i in range(n-1):
            if res[i]>=res[i+1]:
                return False
        return True
        
