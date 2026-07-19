# Problem: Design HashMap
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class MyHashMap(object):

    def __init__(self):
        self.d={}
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.d[key]=value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        else:
            return self.d[key]
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.d:
            self.d.pop(key) 
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
