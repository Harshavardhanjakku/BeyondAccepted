# Problem: Combination Sum
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 2

class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        n = len(candidates)
        def mysum(idx, temp, targetsum):
            if targetsum == 0:
                res.append(temp[:])  
                return
            if targetsum < 0 or idx >= n:
                return
            temp.append(candidates[idx])
            mysum(idx, temp, targetsum - candidates[idx])
            temp.pop()
            mysum(idx + 1, temp, targetsum)

        mysum(0, [], target)
        return res
