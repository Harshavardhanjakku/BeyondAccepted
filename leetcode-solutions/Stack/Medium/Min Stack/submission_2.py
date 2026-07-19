# Problem: Min Stack
# Difficulty: Medium
# Topic: Stack
# Language: python
# Submission: 2

class MinStack(object):

    def __init__(self):
        self.TOP=-1
        self.mystack=[]
        self.mymin=float('inf')

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.mystack.append(value)
        self.TOP+=1
        self.mymin=min(self.mymin,value)
        

    def pop(self):
        """
        :rtype: None
        """
        self.mystack.pop()
        self.TOP-=1
        if self.mystack:
            self.mymin=min(self.mystack)
        else:
            self.mymin=float('inf')
    def top(self):
        """
        :rtype: int
        """
        return self.mystack[self.TOP]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mymin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
