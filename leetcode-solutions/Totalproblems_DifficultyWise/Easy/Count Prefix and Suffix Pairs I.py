# Count Prefix and Suffix Pairs I
# Difficulty: Easy
# Language: python

class Solution(object):
    def countPrefixSuffixPairs(self, words):
        def isPrefixAndSuffix(str1,str2,m):
            return str1==str2[:m] and str1==str2[-m:]
        n=len(words)
        count=0
        for i in range(n):
            for j in range(i+1,n):
                m=len(words[i])
                if m<=len(words[j]) and isPrefixAndSuffix(words[i],words[j],m):
                    count+=1
        return count
