# Decode the Message
# Difficulty: Easy
# Language: python

class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        key=key.replace(" ","")
        msg=""
        dic={} 
        count=0
        for value in key:
            if value not in dic :
                dic[value]=count
                msg+=value 
                count+=1
        print(dic)
        print(msg)
        s=""
        for i in message :
            if i==" ":
                s+=i
            else:
                ind=dic[i]
                s+=chr(ind+97)
        return s
