# Problem: Max Sum of a Pair With Equal Sum of Digits
# Difficulty: Medium
# Topic: Array
# Language: python
# Submission: 1

class Solution(object):
    def maximumSum(self, nums):
        def digit_sum(n):
            s = n
            temp = n
            while temp:
                temp //= 10
                s -= 9 * temp
            return s
        lst = [[] for _ in range(82)]
        for i in nums:
            lst[digit_sum(i)].append(i)
        tot = -1
        for l in lst:
            if len(l) >= 2:
                l.sort(reverse=True)
                tot = max(tot, l[0] + l[1])
        return tot
