# Binary Tree Zigzag Level Order Traversal
# Difficulty: Medium
# Language: python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        from collections import deque
        q=deque()
        res=[]
        flag=True
        if not root :
            return res 
        q.append([root])
        while q :
            nodelist=q.popleft()
            datalist=[]
            templist=[]
            for node in nodelist :
                datalist.append(node.val)
                if node.left:
                    templist.append(node.left) 
                if node.right:
                    templist.append(node.right) 
            if templist:
                q.append(templist)
            if flag:
                res.append(datalist)
            else:
                res.append(datalist[::-1])
            flag=not flag
        return res


