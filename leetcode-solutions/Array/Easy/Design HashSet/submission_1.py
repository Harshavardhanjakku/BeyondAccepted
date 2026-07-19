# Problem: Design HashSet
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class MyHashSet(object):

    def __init__(self):
        self.d=set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.d.add(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.d:
            self.d.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.d
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
