# Problem: Lemonade Change
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 3

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dic={"5":0,"10":0,"20":0}
        for i in bills:
            if i==5:
                dic["5"]+=1
            elif i==10:
                dic["10"]+=1
                if dic["5"]==0:
                    print("5 Case Fail")
                    return False
                else:
                    dic["5"]-=1
            else:
                dic["20"]+=1
                if dic["10"] and dic["5"]:
                    dic["10"]-=1
                    dic["5"]-=1
                elif dic["5"]>=3:
                    dic["5"]-=3
                else:
                    return False
        return True

