# Minimum Index Sum of Two Lists
# Difficulty: Easy
# Language: python

class Solution(object):
    def findRestaurant(self, list1, list2):
        dic = {v: i for i, v in enumerate(list1)}
        minidx = float('inf')
        res = []
        
        for i, v in enumerate(list2):
            if v in dic:
                s = i + dic[v]
                if s < minidx:
                    minidx = s
                    res = [v]
                elif s == minidx:
                    res.append(v)
        
        return res
