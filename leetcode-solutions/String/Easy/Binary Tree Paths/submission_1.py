# Problem: Binary Tree Paths
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        res=[]
        def dfs(root,temp):
            if not root:
                return
            temp.append(root.val)
            if root.left is None and root.right is None:
                res.append("->".join(map(str,temp)))
                return
            dfs(root.left,temp[:])
            dfs(root.right,temp[:])
        dfs(root,[])
        return res
