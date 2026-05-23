# Problem: Minimum Index Sum of Two Lists
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def findRestaurant(self, list1, list2):
        dic = {} 
        for idx, val in enumerate(list1):
            dic[val] = idx
        minidx = float('inf') 
        for idx, val in enumerate(list2):
            if val in dic:
                if dic[val] + idx <= minidx:
                    minidx = dic[val] + idx
        res = [] 
        for idx, val in enumerate(list2):
            if val in dic and dic[val] + idx == minidx:
                res.append(val)
        return res
