# Problem: Reformat Date
# Difficulty: Easy
# Topic: String
# Language: python
# Submission: 2

class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        dic={"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        l=date.split()
        if len(l[0][:-2])==2:
            return l[-1]+"-"+dic[l[1]]+"-"+l[0][:-2]
        else:
            return l[-1]+"-"+dic[l[1]]+"-"+"0"+l[0][:-2]
        
