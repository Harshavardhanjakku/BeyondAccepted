# Problem: Find X-Sum of All K-Long Subarrays I
# Difficulty: Easy
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def findXSum(self, nums, k, x):
        n=len(nums)
        ans=[]
        for start in range(n-k+1):
            dic={}
            sub=nums[start:start+k]
            for v in sub:
                if v not in dic:
                    dic[v]=1
                else:
                    dic[v]+=1
            dic=sorted(dic.items(), key=lambda item: (item[1], item[0]), reverse=True)
            s=0
            cnt=0
            for val,freq in dic:
                if cnt==x:
                    break
                s+=val*freq
                cnt+=1
            ans.append(s)
        return ans

