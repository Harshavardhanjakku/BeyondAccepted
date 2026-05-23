# Problem: Binary Tree Level Order Traversal
# Difficulty: Medium
# Topic: Tree
# Language: python
# Submission: 2

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            datalist = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                datalist.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(datalist)
        return res

