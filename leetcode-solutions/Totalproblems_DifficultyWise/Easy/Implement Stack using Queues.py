# Implement Stack using Queues
# Difficulty: Easy
# Language: python3

class MyStack: 
    def __init__(self):
        
        self.mystack=[]
    def push(self, x: int) -> None:
        self.mystack.insert(0,x)
        

    def pop(self) -> int:
        if self.mystack!=[]:
            val=self.mystack[0]
            self.mystack=self.mystack[1::]
            return val
        

    def top(self) -> int:
        val=self.mystack[0]
        return val

        

    def empty(self) -> bool:
        return self.mystack==[]
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
